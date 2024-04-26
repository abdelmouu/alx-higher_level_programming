#!/bin/bash
# Sends a GET request to a URL and displays the body of the response with a custom header
curl -s -X GET "$1" -H "X-School-User-Id: 98"
