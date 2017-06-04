#!/bin/bash
sudo docker run -ti --name $1 -p 5000:5000 -p 5001:5001 -p 5002:5002 --rm --env-file environment $1 $2
