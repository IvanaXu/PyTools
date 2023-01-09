# 2804aa34886ff5b53a6cfeb0fddb392c70a16c8c2144e4f0

basep=~/Documents/PyTools/123.Test_pyperformance_pythonV
regurl=python
ver=$1

cd $basep/Version
mkdir $1
cd ../docker/
ls -l

#
echo ----------------------------------------------
echo build
docker images
docker rmi $regurl:$ver -f
docker build -t $regurl:$ver .
docker images

#
echo ----------------------------------------------
echo test images
docker run --name t$ver -v $basep/Version/$1:/$1 $regurl:$ver sh run.sh $1
docker ps -a
docker rm t$ver -f
docker ps -a

docker system prune --volumes -f
rm -rf $basep/Version/$1/venv
