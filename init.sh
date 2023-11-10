#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip to proceed."
    exit 1
fi

# Install Python dependencies using pip
python -m pip install --upgrade pip
pip install -r requirements.txt

# Check the exit status of the pip command
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "Failed to install dependencies. Please check the requirements.txt file and try again."
    exit 1
fi