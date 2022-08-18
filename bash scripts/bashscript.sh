#!/bin/bash

echo "Setup and configure server"

file_name=config.yaml
config_dir=$1

if [ -d "$config_dir" ]
then
 echo "reading config directory contents"
 config_files=$(ls "$config_dir")
else 
 echo "config dir not found. Creating one"
 mkdir "$config_dir"
 touch "$config_dir/config.sh"
fi


# example conditional for checking file
# if [ -f "config.yaml" ]

# example conditional for checking numbers
# num_files=xx
# if [ "$num_files" -eq 10 ]

# example conditional for checking strings
user_group=$2
if [ "$user_group" == "nana" ]
then 
 echo "configure the server"
elif [ "$user_group" == "admin" ]
then
	echo "administer the server" 
else
 echo "No permission to configure server. wrong user group"
fi

echo "using file $file_name to configure something"
echo "here are all configuration files: $config_files"

