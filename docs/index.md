# Welcome to SensingPy

**SensingPy** is a Python package for geospatial image processing and analysis, with special focus on remote sensing and bathymetry applications.

## Features

- **Geospatial Image Processing**: Read and process TIFF and NetCDF files
- **Remote Sensing**: Water body detection and analysis
- **Bathymetry Models**: Satellite-derived bathymetry using various models
- **Preprocessing**: Deglinting, outlier detection, and image enhancement
- **Visualization**: Advanced plotting capabilities with cartopy integration
- **Metrics**: Comprehensive validation and error metrics for SDB

## Quick Start

Install sensingpy using pip:

```bash
pip install sensingpy
```

### Basic Usage

```python
from sensingpy import reader, masks
from sensingpy.preprocessing.deglinting import hedley
from sensingpy.bathymetry.models import stumpf_pseudomodel

# Read a geospatial image
img = reader.open("path/to/image.tif")

# Apply preprocessing
img_deglinted = hedley(img)

# Extract water mask
water_mask = masks.water_mask(img)

# Apply bathymetry model
bathymetry = stumpf_pseudomodel(img['blue'], img['green'])
```

## Documentation Structure

- **[User Guide](user_guide/index.md)**: Tutorials and examples using Jupyter notebooks
- **[API Reference](api/index.md)**: Detailed documentation of all modules, classes, and functions

## Getting Help

- [GitHub Repository](https://github.com/Aouei/sensingpy)
- [Issue Tracker](https://github.com/Aouei/sensingpy/issues)

## License

SensingPy is licensed under the GPL-3.0-or-later license.
