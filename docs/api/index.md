# API Reference

Complete API documentation for SensingPy modules, classes, and functions.

# Core Modules

### [Image](image.md)
Core image class for handling geospatial raster data with metadata and coordinate systems.

### [Reader](reader.md)
Functions to read geospatial data from various file formats (TIFF, NetCDF).

### [Selector](selector.md)
Tools for selecting and extracting subsets of data based on spatial or attribute criteria.

### [Masks](masks.md)
Functions to create and apply masks for water bodies, land areas, and other features.

### [Plot](plot.md)
Visualization utilities for displaying geospatial data with maps and custom styling.

### [Enums](enums.md)
Enumeration types used throughout the package for consistent parameter handling.

## Preprocessing

### [preprocessing](preprocessing/index.md)
Image preprocessing and enhancement techniques:

- **[Deglinting](preprocessing/deglinting.md)**: Remove sun glint artifacts
- **[Outliers](preprocessing/outliers.md)**: Detect and handle outlier pixels

## Bathymetry

### [bathymetry](bathymetry/index.md)
Satellite-derived bathymetry models and analysis:

- **[Models](bathymetry/models.md)**: Bathymetry estimation models (Stumpf, etc.)
- **[Metrics](bathymetry/metrics.md)**: Validation metrics and error analysis
- **[Plot](bathymetry/plot.md)**: Specialized plotting for bathymetry results

## Quick Navigation

Use the sidebar navigation to browse through the API documentation. Each page includes:

- Function/class signatures
- Detailed descriptions
- Parameter specifications
- Return value descriptions
- Usage examples (where available)
- Source code links
