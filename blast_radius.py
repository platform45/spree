#!/usr/bin/env python3
"""
Blast Radius Visualization Script for Spree Repository

This script generates a dependency visualization for the Spree repository
using dep-tree, a tool for visualizing code dependencies.

Requirements:
- Python 3.7+
- dep-tree (install with: pip install python-dep-tree)

Usage:
    python blast_radius.py [directory]

Example:
    python blast_radius.py core
    python blast_radius.py frontend
    python blast_radius.py api
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def find_entry_points(directory):
    """Find potential entry points in the given directory."""
    entry_points = []
    
    # Common entry point patterns
    patterns = [
        "**/*.rb",       # Ruby files
        "**/lib/**/*.rb", # Ruby library files
        "**/app/**/*.rb", # Ruby application files
    ]
    
    for pattern in patterns:
        for file_path in Path(directory).glob(pattern):
            # Skip test files
            if "spec/" in str(file_path) or "test/" in str(file_path):
                continue
            
            # Check if file might be an entry point (contains class or module definitions)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                try:
                    content = f.read()
                    if "class " in content or "module " in content:
                        entry_points.append(str(file_path))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    # Sort by file size (smaller files are more likely to be entry points)
    entry_points.sort(key=lambda x: os.path.getsize(x))
    
    # Return the top 5 potential entry points
    return entry_points[:5]

def generate_visualization(directory=None):
    """Generate dependency visualization for the specified directory."""
    try:
        # Check if dep-tree is installed
        subprocess.run(["dep-tree", "--version"], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("dep-tree is not installed. Installing...")
        try:
            subprocess.run(["pip", "install", "python-dep-tree"], check=True)
        except subprocess.CalledProcessError:
            print("Failed to install dep-tree. Please install it manually:")
            print("pip install python-dep-tree")
            return False
    
    # Determine which directory to analyze
    if not directory:
        print("Available directories to analyze:")
        print("1. core")
        print("2. frontend")
        print("3. backend")
        print("4. api")
        print("5. lib")
        choice = input("Select a directory to analyze (1-5) or enter a custom path: ")
        
        if choice == "1":
            directory = "core"
        elif choice == "2":
            directory = "frontend"
        elif choice == "3":
            directory = "backend"
        elif choice == "4":
            directory = "api"
        elif choice == "5":
            directory = "lib"
        else:
            directory = choice
    
    # Find entry points
    print(f"Finding entry points in {directory}...")
    entry_points = find_entry_points(directory)
    
    if not entry_points:
        print(f"No entry points found in {directory}. Please specify a file manually.")
        return False
    
    print("Found potential entry points:")
    for i, entry_point in enumerate(entry_points, 1):
        print(f"{i}. {entry_point}")
    
    choice = input("Select an entry point (1-5) or enter a custom file path: ")
    
    try:
        entry_point = entry_points[int(choice) - 1]
    except (ValueError, IndexError):
        entry_point = choice
    
    # Generate visualization
    print(f"Generating visualization for {entry_point}...")
    try:
        # Create output directory
        output_dir = "blast_radius_output"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate the visualization with enhanced options
        subprocess.run([
            "dep-tree", 
            "entropy", 
            entry_point,
            "--output", f"{output_dir}/dependency_graph.html",
            "--depth", "5",  # Limit depth for better performance
            "--include", "*.rb",  # Focus on Ruby files
        ], check=True)
        
        # Open the visualization in the browser
        html_path = os.path.abspath(f"{output_dir}/dependency_graph.html")
        print(f"Visualization saved to: {html_path}")
        webbrowser.open(f"file://{html_path}")
        
        print("Visualization generated successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error generating visualization: {e}")
        return False

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else None
    generate_visualization(directory)