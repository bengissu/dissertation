#!/bin/bash

# Specify the base URL
BASE_URL="https://www.astro.cf.ac.uk/~spxap/aow/participants"

# Define the output directory
OUTPUT_DIRECTORY="/path/welshdata/videos"

# Loop through participant numbers (01-20)
for participant in $(seq -w 01 20); do
    # Loop through set numbers (01-10)
    for set_number in $(seq -w 01 10); do
        # Check if both participant and set_number are 01
        if [ "$participant" = "01" ] && [ "$set_number" = "01" ]; then
            continue
        fi

        # Construct the URL
        URL="${BASE_URL}/${participant}/sets/${set_number}.mp4#t=0.1"
        # Define the destination file name
        FILENAME="participant_${participant}_sets_${set_number}.mp4"
        # Download the file using wget and specify the output filename
        wget -nc "$URL" -P "$OUTPUT_DIRECTORY" -O "$OUTPUT_DIRECTORY/$FILENAME"
    done
done
