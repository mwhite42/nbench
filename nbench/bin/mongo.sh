#!/usr/bin/env bash

docker run -d -p 27017:27107 -n -v ~/data:/data/db mongo
