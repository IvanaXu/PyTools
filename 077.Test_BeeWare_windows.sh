#
md beeware-tutorial
cd beeware-tutorial
python -m venv beeware-venv
beeware-venv\Scripts\activate.bat

#
python -m pip install briefcase -i https://pypi.tuna.tsinghua.edu.cn/simple

#
briefcase new

#
cd helloworld
briefcase dev

#
briefcase create

#
briefcase build

#
briefcase run

#
briefcase package
