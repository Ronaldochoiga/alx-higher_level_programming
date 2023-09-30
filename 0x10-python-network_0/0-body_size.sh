#!/bin/bash
# This script shows the size of url request. The script uses curl command.
curl -s -w %{size_download}"\n" "$1" -o /dev/null
