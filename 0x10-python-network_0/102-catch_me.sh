#!/bin/bash
# Makes a request that causes the server to respond with "You got me!"
curl -s -X GET 0.0.0.0:5000/catch_me -L -w "%{http_code}" -o /dev/null | grep -Eq "^200$"
curl -s -X GET 0.0.0.0:5000/catch_me

