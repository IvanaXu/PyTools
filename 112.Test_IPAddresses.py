#
import ipaddress

# ipaddress
ip0 = ipaddress.IPv4Address('192.168.0.1')
print(type(ip0), isinstance(ip0, ipaddress.IPv4Address))

ip1 = ipaddress.IPv4Address(3232235521)
ip2 = ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
print(ip0 == ip1 == ip2)

print(ip0.reverse_pointer)

print(format(ip0))

print(ipaddress.IPv4Address('127.0.0.2') > ipaddress.IPv4Address('127.0.0.1'))

print(ipaddress.IPv4Address('127.0.0.2') + 3)

# ip_network
ipn = ipaddress.ip_network('192.0.2.0/29')
print(ipn)
print([_ip for _ip in ipn.hosts()])

# interface
ipf = ipaddress.IPv4Interface('192.0.2.5/24')
print(ipf)
print(ipf.ip, ipf.network)
