#!/bin/bash

# Send a POST request to the catch_me endpoint with a specific user-agent header
curl -s -X POST -H "User-Agent: I am a hacker" "http://0.0.0.0:5000/catch_me"
