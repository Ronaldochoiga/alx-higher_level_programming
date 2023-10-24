#!/bin/bash
#sends a request to a URL and shows status code only
curl -sX HEAD -w "%{http_code}" "$1"
