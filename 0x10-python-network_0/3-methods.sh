#!/bin/bash
# This script performs the allow process where it takes a url and shows all the verbs and methods accepted by it.
curl -sI "$1" | grep Allow | cut -d " " -f 2-
