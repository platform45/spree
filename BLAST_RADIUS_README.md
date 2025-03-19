# Blast Radius Visualization for Spree

This tool helps you visualize the dependencies and "blast radius" of changes in your Spree codebase. It uses [dep-tree](https://github.com/gabotechs/dep-tree) to generate interactive 3D visualizations of code dependencies.

## What is Blast Radius?

"Blast radius" refers to the scope of impact that changes to a particular file or component might have on the rest of the codebase. By visualizing dependencies between files, you can:

1. Understand which parts of the codebase are most interconnected
2. Identify potential refactoring opportunities
3. Assess the risk of changes to specific components
4. Discover architectural patterns and anti-patterns

## Requirements

- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

## Installation

No installation is required. The script will automatically install the necessary dependencies (dep-tree) if they're not already installed.

## Usage

### Option 1: Using the Shell Script (Recommended)

1. Make the script executable:
   ```
   chmod +x visualize_dependencies.sh
   ```

2. Run the script with an optional directory parameter:
   ```
   ./visualize_dependencies.sh [directory]
   ```

   For example:
   ```
   ./visualize_dependencies.sh core
   ./visualize_dependencies.sh frontend
   ./visualize_dependencies.sh api
   ```

3. If you don't specify a directory, the script will prompt you to choose one.

4. The script will find potential entry points in the selected directory and prompt you to choose one.

5. A browser window will open with the interactive 3D visualization.

### Option 2: Using the Python Script Directly

1. Run the Python script:
   ```
   python3 blast_radius.py [directory]
   ```

## Interpreting the Visualization

The visualization shows files as spheres and dependencies as lines between them:

- **Spheres (Nodes)**: Each sphere represents a file in your codebase.
- **Lines (Edges)**: Each line represents a dependency between files.
- **Clusters**: Files that are tightly coupled tend to cluster together.
- **Isolated Nodes**: Files with few dependencies appear more isolated.
- **Colors**: The colors represent different types of relationships between files.
  - **Red**: Files with many dependencies (high risk when changing)
  - **Green**: Files with few dependencies (lower risk when changing)
  - **Yellow/Orange**: Files with moderate dependencies

### Interaction

- **Zoom**: Scroll to zoom in/out
- **Rotate**: Click and drag to rotate the view
- **Pan**: Right-click and drag to pan
- **Select**: Click on a node to highlight its direct dependencies
- **Details**: Hover over a node to see its filename and additional information

## Output Files

All visualization files are saved in the `blast_radius_output` directory:

- `dependency_graph.html`: The main interactive visualization
- Additional supporting files may be generated depending on the complexity of the codebase

## Tips for Effective Analysis

1. **Start with Core Components**: Begin by analyzing core directories to understand the foundation of your application.

2. **Compare Different Modules**: Analyze different modules separately to compare their architectural patterns.

3. **Look for Clusters**: Dense clusters indicate tightly coupled code that might benefit from refactoring.

4. **Identify Central Nodes**: Files with many connections are central to your application and changes to them may have a wide impact.

5. **Find Isolated Components**: Components with few connections are more isolated and safer to modify.

6. **Focus on Specific Areas**: Use the depth parameter to focus on specific areas of the codebase.

7. **Compare Before and After**: Generate visualizations before and after refactoring to see the impact of your changes.

## Advanced Usage

### Customizing the Visualization

You can modify the `blast_radius.py` script to customize the visualization:

- Change the `--depth` parameter to control how deep the dependency analysis goes
- Modify the `--include` parameter to focus on specific file types
- Add additional parameters to the `dep-tree` command for more customization

### Batch Processing

You can create a batch script to generate visualizations for multiple directories:

```bash
#!/bin/bash
for dir in core frontend backend api; do
  ./visualize_dependencies.sh $dir
done
```

## Troubleshooting

- If you encounter errors related to file encoding, try running the script on a subset of files or a specific directory.
- If the visualization doesn't open automatically, check the console output for any error messages.
- For large codebases, the visualization might take some time to generate and might be resource-intensive to render.
- If you see "Command not found" errors, make sure the scripts are executable (`chmod +x blast_radius.py visualize_dependencies.sh`).

## Additional Resources

- [dep-tree GitHub Repository](https://github.com/gabotechs/dep-tree)
- [Code Dependency Visualization Best Practices](https://www.codesee.io/blog/code-dependency-visualization-best-practices)
- [Understanding Software Architecture with Dependency Analysis](https://martinfowler.com/articles/dependency-analysis.html)