v=centos:latest

echo $v

docker stop itest

docker rm itest

docker run -ti -v /Users/ivan/Desktop:/data --name itest $v /bin/bash
