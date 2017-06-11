#!/bin/bash
sudo docker run -ti --name $1 -p 5000:5000 -p 5001:5001 -p 5002:5002 -v /home/pablo/github/econo2/login/docker/src:/src --rm --env-file ../../../../gitlab/fce/casa-pablo/environment-casa $1 $2
