#!/bin/bash

# Create a header for the file
echo "App Name,File Size (KB),Date Modified" > mac_applications_folder.txt

# Get the path to the Applications folder
applications_path="/Applications"

# Iterate over all files in the Applications folder, filtering for application bundles
find "$applications_path" -type d -name "*.app" -print0 | while IFS= read -r -d $'\0' app_folder; do

  # Get the application name from the folder name
  app_name=$(basename "$app_folder" .app)

  # Get the file size in KB
  file_size=$(du -sk "$app_folder" | awk '{print $1}')

  # Get the date modified (using a more compatible format)
  date_modified=$(stat -f %m "$app_folder" | date +"%Y-%m-%d %H:%M:%S")

  # Write the data to the file
  echo "$app_name,$file_size,$date_modified" >> mac_applications_folder.txt

done