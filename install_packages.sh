#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Please install Python and pip first."
    exit 1
fi

# Install dhooks-lite and websocket-client
pip install dhooks-lite websocket-client
