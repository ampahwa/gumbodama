#!/bin/bash

export passwd=soupman #must hide later
export db="gumbotdb"
export collect="soup"
export key="soupName"

python3 mongo_port.py $db $collect $key $passwd