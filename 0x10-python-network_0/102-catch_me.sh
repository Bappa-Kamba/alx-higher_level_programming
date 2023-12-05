#!/bin/bash
curl -s -X POST -H "Content-Type: application/json" -d '{"key": "You got me!"}' http://0.0.0.0:5000/catch_me
