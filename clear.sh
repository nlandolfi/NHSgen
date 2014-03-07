#!/bin/bash

while true; do
    read -p "Are you sure you want to DELETE all applications?" yn
    case $yn in
        [Yy]* ) rm -rf applications/*.html; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


