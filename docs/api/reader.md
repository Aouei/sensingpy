# Reader Module

`sensingpy.reader` provides classes for loading geospatial raster data from
NetCDF and GeoTIFF files, plus a convenience `open()` function that dispatches
to the right reader automatically.

---

## ImageReader

Base class that defines the common interface for all readers.

::: sensingpy.reader.ImageReader
    options:
      show_source: true
      heading_level: 3
      members_order: source
      show_if_no_docstring: true
      group_by_category: true
      show_category_heading: true
      show_symbol_type_heading: true
      show_symbol_type_toc: true
      filters:
        - "!^_"

---

## NetCDFReader

Reads multidimensional NetCDF files and exposes bands as `Image` objects.

::: sensingpy.reader.NetCDFReader
    options:
      show_source: true
      heading_level: 3
      members_order: source
      show_if_no_docstring: true
      group_by_category: true
      show_category_heading: true
      show_symbol_type_heading: true
      show_symbol_type_toc: true
      filters:
        - "!^_"

---

## GeoTIFFReader

Reads single- or multi-band GeoTIFF files and exposes bands as `Image` objects.

::: sensingpy.reader.GeoTIFFReader
    options:
      show_source: true
      heading_level: 3
      members_order: source
      show_if_no_docstring: true
      group_by_category: true
      show_category_heading: true
      show_symbol_type_heading: true
      show_symbol_type_toc: true
      filters:
        - "!^_"

---

## open

::: sensingpy.reader.open
