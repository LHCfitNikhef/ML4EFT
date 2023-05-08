#!/bin/sh
coefficient="$1"

cd /data/theorie/pherbsch/ML4EFT/subproj/code/

# Update the runcard with the coefficient given by the init file. 
# sed searches for the sequence of the coefficient and replaces it with the new coefficient

sed -i "s/\"coefficient\": \".*\"/\"coefficient\": \"$coefficient\"/" ./runcards/shower/shower_settings.json

cat ../code/runcards/shower/shower_settings.json