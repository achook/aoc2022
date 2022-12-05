#!/usr/bin/env bash

# Check if it's december
month=$( date +%m )

if [ $month != 12 ]; then
    echo "Sorry, it's not december"
    return 1
fi

# Generate tiles
cd ./.tiles
source env/usr/local/bin/activate
python3.11 generator.py
deactivate
cd ..

# Get current day
day_nozero=$( date +%-d )

git add .
git commit -m "Add day $day_nozero"