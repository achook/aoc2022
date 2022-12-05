#!/usr/bin/env bash

# Check if it's december
month=$( date +%m )

if [ $month != 12 ]; then
    echo "Sorry, it's not december"
    return 1
fi

# Get current day
day=$( date +%0d )
day_nozero=$( date +%-d )

# Make a directory for the date, but only if it doesn't exist
mkdir -p $day

# Move into the directory
cd $day

# Download a test file and save it as input.txt
url=https://adventofcode.com/2022/day/"$day_nozero"/input
cookie="Cookie: session=""$(cat ../.tiles/session.cookie)"
curl $url \
-H $cookie \
-o input.txt -s

cd ..