#!/bin/bash

# Blast Radius Visualization Script for Spree Repository
# This script helps visualize code dependencies in the Spree repository

# Set script to exit on error
set -e

# Print colored messages
function print_info() {
    echo -e "\033[0;34m[INFO]\033[0m $1"
}

function print_success() {
    echo -e "\033[0;32m[SUCCESS]\033[0m $1"
}

function print_error() {
    echo -e "\033[0;31m[ERROR]\033[0m $1"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    print_error "pip is required but not installed. Please install pip and try again."
    exit 1
fi

# Install dep-tree if not already installed
if ! command -v dep-tree &> /dev/null; then
    print_info "Installing dep-tree..."
    pip install python-dep-tree
    if [ $? -ne 0 ]; then
        print_error "Failed to install dep-tree. Please install it manually: pip install python-dep-tree"
        exit 1
    fi
    print_success "dep-tree installed successfully!"
fi

# Make sure the Python script is executable
chmod +x blast_radius.py

# Create output directory if it doesn't exist
mkdir -p blast_radius_output

# Run the Python script
print_info "Running Blast Radius visualization..."
python3 blast_radius.py "$@"

# Check if the script ran successfully
if [ $? -eq 0 ]; then
    print_success "Visualization completed successfully!"
    print_info "Check the 'blast_radius_output' directory for the generated files."
else
    print_error "Visualization failed. Please check the error messages above."
    exit 1
fi