#
docker pull nicolargo/glances:dev

#
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock:ro --pid host --network host -it nicolargo/glances:dev

#
# q
