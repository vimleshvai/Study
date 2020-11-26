#!/bin/bash

var= jq .prefixes[].ip_prefix||region ip-ranges.json

echo "$var"

'''
var1= jq .prefixes[].region ip-ranges.json

echo "$var1"
'''

