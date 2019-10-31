#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rsalite by ino@o3or.com
#===========================================================================
#  Copyright 2011 Sybren A. Stüvel <sybren@stuvel.eu>
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#===========================================================================
"""
RSALite module

Module for calculating large primes, and RSA encryption, decryption. 
not includes generating public and private keys.

"""
from __future__ import absolute_import
import sys
import binascii
import hashlib
import os
from struct import pack

__author__ = "Sybren Stuvel, Barry Mead and Yesudeep Mangalapilly | lite by ino"
__date__ = "2014-03-28"
__version__ = '3.1.4lite'

# ===========================================================================
#"""Python compatibility wrappers."""


try:
    MAX_INT = sys.maxsize
except AttributeError:
    MAX_INT = sys.maxint

MAX_INT64 = (1 << 63) - 1
MAX_INT32 = (1 << 31) - 1
MAX_INT16 = (1 << 15) - 1

# Determine the word size of the processor.
if MAX_INT == MAX_INT64:
    # 64-bit processor.
    MACHINE_WORD_SIZE = 64
elif MAX_INT == MAX_INT32:
    # 32-bit processor.
    MACHINE_WORD_SIZE = 32
else:
    # Else we just assume 64-bit processor keeping up with modern times.
    MACHINE_WORD_SIZE = 64


try:
    # < Python3
    unicode_type = unicode
    have_python3 = False
except NameError:
    # Python3.
    unicode_type = str
    have_python3 = True

# Fake byte literals.
if str is unicode_type:
    def byte_literal(s):
        return s.encode('latin1')
else:
    def byte_literal(s):
        return s

# ``long`` is no more. Do type detection using this instead.
try:
    integer_types = (int, long)
except NameError:
    integer_types = (int,)

b = byte_literal


# To avoid calling b() multiple times in tight loops.
ZERO_BYTE = b('\x00')
EMPTY_BYTE = b('')


def is_integer(obj):
    """
    Determines whether the given value is an integer.

    :param obj:
        The value to test.
    :returns:
        ``True`` if ``value`` is an integer; ``False`` otherwise.
    """
    return isinstance(obj, integer_types)

def get_word_alignment(num, force_arch=64,
                       _machine_word_size=MACHINE_WORD_SIZE):
    """
    Returns alignment details for the given number based on the platform
    Python is running on.

    :param num:
        Unsigned integral number.
    :param force_arch:
        If you don't want to use 64-bit unsigned chunks, set this to
        anything other than 64. 32-bit chunks will be preferred then.
        Default 64 will be used when on a 64-bit machine.
    :param _machine_word_size:
        (Internal) The machine word size used for alignment.
    :returns:
        4-tuple::

            (word_bits, word_bytes,
             max_uint, packing_format_type)
    """
    max_uint64 = 0xffffffffffffffff
    max_uint32 = 0xffffffff
    max_uint16 = 0xffff
    max_uint8 = 0xff

    if force_arch == 64 and _machine_word_size >= 64 and num > max_uint32:
        # 64-bit unsigned integer.
        return 64, 8, max_uint64, "Q"
    elif num > max_uint16:
        # 32-bit unsigned integer
        return 32, 4, max_uint32, "L"
    elif num > max_uint8:
        # 16-bit unsigned integer.
        return 16, 2, max_uint16, "H"
    else:
        # 8-bit unsigned integer.
        return 8, 1, max_uint8, "B"

# ===========================================================================
# '''Common functionality shared by several modules.'''


def bit_size(num):
    '''
    Number of bits needed to represent a integer excluding any prefix
    0 bits.

    As per definition from http://wiki.python.org/moin/BitManipulation and
    to match the behavior of the Python 3 API.

    Usage::
    
        >>> bit_size(1023)
        10
        >>> bit_size(1024)
        11
        >>> bit_size(1025)
        11

    :param num:
        Integer value. If num is 0, returns 0. Only the absolute value of the
        number is considered. Therefore, signed integers will be abs(num)
        before the number's bit length is determined.
    :returns:
        Returns the number of bits in the integer.
    '''
    if num == 0:
        return 0
    if num < 0:
        num = -num

    # Make sure this is an int and not a float.
    num & 1

    hex_num = "%x" % num
    return ((len(hex_num) - 1) * 4) + {
        '0':0, '1':1, '2':2, '3':2,
        '4':3, '5':3, '6':3, '7':3,
        '8':4, '9':4, 'a':4, 'b':4,
        'c':4, 'd':4, 'e':4, 'f':4,
     }[hex_num[0]]


def byte_size(number):
    '''
    Returns the number of bytes required to hold a specific long number.
    
    The number of bytes is rounded up.

    Usage::

        >>> byte_size(1 << 1023)
        128
        >>> byte_size((1 << 1024) - 1)
        128
        >>> byte_size(1 << 1024)
        129

    :param number:
        An unsigned integer
    :returns:
        The number of bytes required to hold a specific long number.
    '''
    quanta, mod = divmod(bit_size(number), 8)
    if mod or number == 0:
        quanta += 1
    return quanta
    #return int(math.ceil(bit_size(number) / 8.0))

# ===========================================================================

#'''Core mathematical operations.

#This is the actual core RSA implementation, which is only defined
#mathematically on integers.
#'''

def assert_int(var, name):

    if is_integer(var):
        return

    raise TypeError('%s should be an integer, not %s' % (name, var.__class__))

def encrypt_int(message, ekey, n):
    '''Encrypts a message using encryption key 'ekey', working modulo n'''

    assert_int(message, 'message')
    assert_int(ekey, 'ekey')
    assert_int(n, 'n')

    if message < 0:
        raise ValueError('Only non-negative numbers are supported')
     
    if message > n:
        raise OverflowError("The message %i is too long for n=%i" % (message, n))

    return pow(message, ekey, n)

def decrypt_int(cyphertext, dkey, n):
    '''Decrypts a cypher text using the decryption key 'dkey', working
    modulo n'''

    assert_int(cyphertext, 'cyphertext')
    assert_int(dkey, 'dkey')
    assert_int(n, 'n')

    message = pow(cyphertext, dkey, n)
    return message

# ===========================================================================

#'''Data transformation functions.

#From bytes to a number, number to bytes, etc.
#'''



try:
    # We'll use psyco if available on 32-bit architectures to speed up code.
    # Using psyco (if available) cuts down the execution time on Python 2.5
    # at least by half.
    import psyco
    psyco.full()
except ImportError:
    pass



def bytes2int(raw_bytes):
    r'''Converts a list of bytes or an 8-bit string to an integer.

    When using unicode strings, encode it to some encoding like UTF8 first.

    >>> (((128 * 256) + 64) * 256) + 15
    8405007
    >>> bytes2int('\x80@\x0f')
    8405007

    '''

    return int(binascii.hexlify(raw_bytes), 16)


def bytes_leading(raw_bytes, needle=ZERO_BYTE):
    '''
    Finds the number of prefixed byte occurrences in the haystack.

    Useful when you want to deal with padding.

    :param raw_bytes:
        Raw bytes.
    :param needle:
        The byte to count. Default \000.
    :returns:
        The number of leading needle bytes.
    '''
    leading = 0
    # Indexing keeps compatibility between Python 2.x and Python 3.x
    _byte = needle[0]
    for x in raw_bytes:
        if x == _byte:
            leading += 1
        else:
            break
    return leading


def int2bytes(number, fill_size=None, chunk_size=None, overflow=False):
    '''
    Convert an unsigned integer to bytes (base-256 representation)::

    Does not preserve leading zeros if you don't specify a chunk size or
    fill size.

    .. NOTE:
        You must not specify both fill_size and chunk_size. Only one
        of them is allowed.

    :param number:
        Integer value
    :param fill_size:
        If the optional fill size is given the length of the resulting
        byte string is expected to be the fill size and will be padded
        with prefix zero bytes to satisfy that length.
    :param chunk_size:
        If optional chunk size is given and greater than zero, pad the front of
        the byte string with binary zeros so that the length is a multiple of
        ``chunk_size``.
    :param overflow:
        ``False`` (default). If this is ``True``, no ``OverflowError``
        will be raised when the fill_size is shorter than the length
        of the generated byte sequence. Instead the byte sequence will
        be returned as is.
    :returns:
        Raw bytes (base-256 representation).
    :raises:
        ``OverflowError`` when fill_size is given and the number takes up more
        bytes than fit into the block. This requires the ``overflow``
        argument to this function to be set to ``False`` otherwise, no
        error will be raised.
    '''
    if number < 0:
        raise ValueError("Number must be an unsigned integer: %d" % number)

    if fill_size and chunk_size:
        raise ValueError("You can either fill or pad chunks, but not both")

    # Ensure these are integers.
    number & 1

    raw_bytes = b('')

    # Pack the integer one machine word at a time into bytes.
    num = number
    word_bits, _, max_uint, pack_type = get_word_alignment(num)
    pack_format = ">%s" % pack_type
    while num > 0:
        raw_bytes = pack(pack_format, num & max_uint) + raw_bytes
        num >>= word_bits
    # Obtain the index of the first non-zero byte.
    zero_leading = bytes_leading(raw_bytes)
    if number == 0:
        raw_bytes = ZERO_BYTE
    # De-padding.
    raw_bytes = raw_bytes[zero_leading:]

    length = len(raw_bytes)
    if fill_size and fill_size > 0:
        if not overflow and length > fill_size:
            raise OverflowError(
                "Need %d bytes for number, but fill size is %d" %
                (length, fill_size)
            )
        raw_bytes = raw_bytes.rjust(fill_size, ZERO_BYTE)
    elif chunk_size and chunk_size > 0:
        remainder = length % chunk_size
        if remainder:
            padding_size = chunk_size - remainder
            raw_bytes = raw_bytes.rjust(length + padding_size, ZERO_BYTE)
    return raw_bytes


# ===========================================================================
#'''RSA key code.

#Create new keys with the newkeys() function. It will give you a PublicKey and a
#PrivateKey object.

#Loading and saving keys requires the pyasn1 module. This module is imported as
#late as possible, such that other functionality will remain working in absence
#of pyasn1.

#'''

class PublicKey():
    '''Represents a public RSA key.

    This key is also known as the 'encryption key'. It contains the 'n' and 'e'
    values.

    Supports attributes as well as dictionary-like access. Attribute accesss is
    faster, though.

    >>> PublicKey(5, 3)
    PublicKey(5, 3)

    >>> key = PublicKey(5, 3)
    >>> key.n
    5
    >>> key['n']
    5
    >>> key.e
    3
    >>> key['e']
    3

    '''

    __slots__ = ('n', 'e')

    def __init__(self, n, e):
        self.n = n
        self.e = e

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return 'PublicKey(%i, %i)' % (self.n, self.e)

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, PublicKey):
            return False
        return self.n == other.n and self.e == other.e

    def __ne__(self, other):
        return not (self == other)



class PrivateKey():
    '''Represents a private RSA key.

    This key is also known as the 'decryption key'. It contains the 'n', 'e',
    'd'.

    Supports attributes as well as dictionary-like access. Attribute accesss is
    faster, though.

    >>> PrivateKey(3247, 65537, 833)
    PrivateKey(3247, 65537, 833)

    '''

    __slots__ = ('n', 'e', 'd')

    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return 'PrivateKey(%(n)i, %(e)i, %(d)i' % self

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, PrivateKey):
            return False

        return (self.n == other.n and
            self.e == other.e and
            self.d == other.d)

    def __ne__(self, other):
        return not (self == other)
# ===========================================================================
#'''Functions for PKCS#1 version 1.5 encryption and signing

#This module implements certain functionality from PKCS#1 version 1.5. For a
#very clear example, read http://www.di-mgt.com.au/rsa_alg.html#pkcs1schemes

#At least 8 bytes of random padding is used when encrypting a message. This makes
#these methods much more secure than the ones in the ``rsa`` module.

#WARNING: this module leaks information when decryption or verification fails.
#The exceptions that are raised contain the Python traceback information, which
#can be used to deduce where in the process the failure occurred. DO NOT PASS
#SUCH INFORMATION to your users.
#'''

class CryptoError(Exception):
    '''Base class for all exceptions in this module.'''

class DecryptionError(CryptoError):
    '''Raised when decryption fails.'''

def _pad_for_encryption(message, target_length):
    r'''Pads the message for encryption, returning the padded message.

    :return: 00 02 RANDOM_DATA 00 MESSAGE

    >>> block = _pad_for_encryption('hello', 16)
    >>> len(block)
    16
    >>> block[0:2]
    '\x00\x02'
    >>> block[-6:]
    '\x00hello'

    '''

    max_msglength = target_length - 11
    msglength = len(message)

    if msglength > max_msglength:
        raise OverflowError('%i bytes needed for message, but there is only'
            ' space for %i' % (msglength, max_msglength))

    # Get random padding
    padding = b('')
    padding_length = target_length - msglength - 3

    # We remove 0-bytes, so we'll end up with less padding than we've asked for,
    # so keep adding data until we're at the correct length.
    while len(padding) < padding_length:
        needed_bytes = padding_length - len(padding)
    
        # Always read at least 8 bytes more than we need, and trim off the rest
        # after removing the 0-bytes. This increases the chance of getting
        # enough bytes, especially when needed_bytes is small
        new_padding = os.urandom(needed_bytes + 5)
        new_padding = new_padding.replace(b('\x00'), b(''))
        padding = padding + new_padding[:needed_bytes]

    assert len(padding) == padding_length

    return b('').join([b('\x00\x02'),
                    padding,
                    b('\x00'),
                    message])


def encrypt(message, pub_key):
    '''Encrypts the given message using PKCS#1 v1.5
    
    :param message: the message to encrypt. Must be a byte string no longer than
        ``k-11`` bytes, where ``k`` is the number of bytes needed to encode
        the ``n`` component of the public key.
    :param pub_key: the :py:class:`rsa.PublicKey` to encrypt with.
    :raise OverflowError: when the message is too large to fit in the padded
        block.
    
    >>> pub_key = PublicKey(n, e)
    >>> message = 'hello'
    >>> crypto = encrypt(message, pub_key)
    
    The crypto text should be just as long as the public key 'n' component:


    '''

    keylength = byte_size(pub_key.n)
    padded = _pad_for_encryption(message, keylength)

    payload = bytes2int(padded)
    encrypted = encrypt_int(payload, pub_key.e, pub_key.n)
    block = int2bytes(encrypted, keylength)

    return block

def decrypt(crypto, priv_key):
    r'''Decrypts the given message using PKCS#1 v1.5

    The decryption is considered 'failed' when the resulting cleartext doesn't
    start with the bytes 00 02, or when the 00 byte between the padding and
    the message cannot be found.

    :param crypto: the crypto text as returned by :py:func:`rsa.encrypt`
    :param priv_key: the :py:class:`rsa.PrivateKey` to decrypt with.
    :raise DecryptionError: when the decryption fails. No details are given as
        to why the code thinks the decryption fails, as this would leak
        information about the private key.

    >>> pub_key = PublicKey(n, e)
    >>> priv_key = PrivateKey(n,e,d)

    It works with strings:

    >>> crypto = encrypt('hello', pub_key)
    >>> decrypt(crypto, priv_key)
    'hello'

    And with binary data:

    >>> crypto = encrypt('\x00\x00\x00\x00\x01', pub_key)
    >>> decrypt(crypto, priv_key)
    '\x00\x00\x00\x00\x01'


    .. warning::

        Never display the stack trace of a
        :py:class:`rsa.pkcs1.DecryptionError` exception. It shows where in the
        code the exception occurred, and thus leaks information about the key.
        It's only a tiny bit of information, but every bit makes cracking the
        keys easier.

    >>> crypto = encrypt('hello', pub_key)
    >>> crypto = crypto[0:5] + 'X' + crypto[6:] # change a byte
    >>> decrypt(crypto, priv_key)
    Traceback (most recent call last):
    ...
    DecryptionError: Decryption failed

    '''

    blocksize = byte_size(priv_key.n)
    encrypted = bytes2int(crypto)
    decrypted = decrypt_int(encrypted, priv_key.d, priv_key.n)
    cleartext = int2bytes(decrypted, blocksize)

    # If we can't find the cleartext marker, decryption failed.
    if cleartext[0:2] != b('\x00\x02'):
        raise DecryptionError('Decryption failed')

    # Find the 00 separator between the padding and the message
    try:
        sep_idx = cleartext.index(b('\x00'), 2)
    except ValueError:
        raise DecryptionError('Decryption failed')

    return cleartext[sep_idx+1:]
# ===========================================================================
def a():
    return 'Yes'