#!/bin/bash
#Makes a request that causes the server to respond with a message
curl -s -L -X PUT -d "user_id:98" -H "Origin:HolbertonShool" 0.0.0.0:5000/catch_me
