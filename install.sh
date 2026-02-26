#!/bin/bash

echo "=== GCP Script Installer ==="

# Check if wget is installed
if ! command -v wget &> /dev/null; then
    echo "wget not found. Installing wget..."
    sudo apt update
    sudo apt install wget -y
    if [ $? -eq 0 ]; then
        echo "wget installed successfully."
    else
        echo "Failed to install wget."
        exit 1
    fi
else
    echo "wget is already installed."
fi

# Delete existing gcp.py if it exists
if [ -f "gcp.py" ]; then
    echo "Deleting old gcp.py file..."
    rm -f gcp.py
    if [ $? -eq 0 ]; then
        echo "Old file deleted successfully."
    else
        echo "Failed to delete old file."
        exit 1
    fi
fi

# Download fresh gcp.py
echo "Downloading fresh gcp.py..."
wget -q --show-progress https://raw.githubusercontent.com/nyeinkokoaung404/cloudshell/refs/heads/main/gcp.py

if [ $? -eq 0 ]; then
    echo "gcp.py downloaded successfully."
    
    # Display file details
    ls -la gcp.py
else
    echo "Failed to download gcp.py."
    exit 1
fi

# Run gcp.py
echo "Running gcp.py..."
python3 gcp.py

if [ $? -eq 0 ]; then
    echo "Script executed successfully."
else
    echo "Failed to run gcp.py."
    exit 1
fi
