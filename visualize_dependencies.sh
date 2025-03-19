#!/bin/bash

# Blast Radius Visualization Script for Spree Repository
# This script helps visualize code dependencies in the Spree repository

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is required but not installed. Please install pip and try again."
    exit 1
fi

# Install dep-tree if not already installed
if ! command -v dep-tree &> /dev/null; then
    echo "Installing dep-tree..."
    pip install python-dep-tree
fi

# Run the Python script
python3 blast_radius.py "$@"