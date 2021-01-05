rm -rf __pycache__

#
python3 099.Test_uncompyle6_source.py

#
python3 -m py_compile 099.Test_uncompyle6_source.py

#
cp __pycache__/099.Test_uncompyle6_source.cpython-36.pyc .

#
python3 099.Test_uncompyle6_source.cpython-36.pyc

rm -rf __pycache__

# /home/admin/.local/bin/uncompyle6 099.Test_uncompyle6_source.cpython-36.pyc