echo -------------------------------- START --------------------------------
cd Temp
ls -l
echo --------------------------------STEP 00--------------------------------
/data/soft/py3/bin/cython
echo --------------------------------STEP 01--------------------------------
# ??? fatal error: Python.h: No such file or directory
# !!! yum upgrade
# !!! yum install python3-devel libusb-devel python36-pyusb.noarch

/data/soft/py3/bin/cython PTest026.py
# /data/soft/py3/bin/python -m py_compile PTest026.py

gcc -c -fPIC PTest026.c
gcc -shared PTest026.o -o PTest026.so
rm -rf PTest026.c PTest026.o

echo --------------------------------STEP 02--------------------------------