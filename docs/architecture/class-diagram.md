# Class Diagram

This page shows the class structure of the SensingPy package.

```mermaid
classDiagram
    direction TB

    %% ── Core ──────────────────────────────────────────────────────────────
    class Image {
        +data : xr.Dataset
        +crs : pyproj.CRS
        +name : str
        +grid_mapping : str
        +band_names : List[str]
        +width : int
        +height : int
        +count : int
        +x_res : float
        +y_res : float
        +transform : Affine
        +bbox : Polygon
        +values : np.ndarray
        +attrs : dict
        +reproject(target_crs, inplace) Image
        +align(other, inplace) Image
        +merge(other) Image
        +resample(scale, inplace) Image
        +clip(geometries, inplace) Image
        +mask(band, value, inplace) Image
        +geometry_mask(geometries, inplace) Image
        +dropna(inplace) Image
        +select(bands) np.ndarray
        +add_band(band_name, data, inplace) Image
        +drop_bands(bands, inplace) Image
        +keep_bands(bands, inplace) Image
        +normalized_diference(band1, band2) np.ndarray
        +extract_values(xs, ys) np.ndarray
        +rename(new_names, inplace) Image
        +rename_by_enum(enum, inplace) Image
        +empty_like() Image
        +copy() Image
        +to_netcdf(filename)
        +to_tif(filename)
    }

    %% ── Readers ───────────────────────────────────────────────────────────
    class ImageReader {
        <<abstract>>
        +read(filename) Image
    }

    class NetCDFReader {
        +read(filename) Image
    }

    class GeoTIFFReader {
        +read(filename) Image
        -_prepare_coords(src, crs, grid_mapping) Dict
        -_prepare_vars(src, coords, grid_mapping) Dict
    }

    %% ── Bathymetry ────────────────────────────────────────────────────────
    class LinearModel {
        +slope : float
        +intercept : float
        +r_square : float
        +fit(pseudomodel, in_situ) Self
        +predict(pseudomodel) np.ndarray
        +predict_and_evaluate(pseudomodel, in_situ) ValidationSummary
    }

    class ValidationSummary {
        <<dataclass>>
        +model : np.ndarray
        +in_situ : np.ndarray
        +error : np.ndarray
        +MSD : float
        +MAE : float
        +MedAE : float
        +RMSE : float
        +RMedSE : float
        +Abs_std : float
        +N : int
    }

    %% ── Enums ─────────────────────────────────────────────────────────────
    class SENTINEL2_BANDS {
        <<enumeration>>
        B1 : 443 nm
        B2 : 493 nm
        B3 : 560 nm
        B4 : 665 nm
        B5 : 704 nm
        B6 : 740 nm
        B7 : 783 nm
        B8 : 833 nm
        B8A : 865 nm
        B9 : 945 nm
        B10 : 1373 nm
        B11 : 1614 nm
        B12 : 2202 nm
    }

    class MICASENSE_BANDS {
        <<enumeration>>
        BLUE
        GREEN
        RED
        NIR
        RED_EDGE
    }

    class FILE_EXTENTIONS {
        <<enumeration>>
        TIF
        NETCDF
    }

    %% ── Function modules ──────────────────────────────────────────────────
    class masks {
        <<module>>
        +is_valid(array) np.ndarray
        +is_lt(array, value) np.ndarray
        +is_gt(array, value) np.ndarray
        +is_eq(array, value) np.ndarray
        +is_lte(array, value) np.ndarray
        +is_gte(array, value) np.ndarray
        +is_in_range(array, vmin, vmax) np.ndarray
    }

    class selector {
        <<module>>
        +interval_choice(array, size, intervals) np.ndarray
        +sample_indices_by_interval(array, size, intervals) np.ndarray
        +composite(arrays, method) np.ndarray
        +composite_indices(arrays, method) np.ndarray
    }

    class deglinting {
        <<module>>
        +hedley(deep_area_mask, to_correct, nir) np.ndarray
        +lyzenga(deep_area_mask, to_correct, nir) np.ndarray
        +joyce(deep_area_mask, to_correct, nir) np.ndarray
    }

    class outliers {
        <<module>>
        +IQR(data, distance) np.ndarray
        +Z_Score(data) np.ndarray
        +upper_percentile(data, percentile) np.ndarray
        +lower_percentile(data, percentile) np.ndarray
    }

    class bathymetry_models {
        <<module>>
        +stumpf_pseudomodel(blue, other, n) np.ndarray
        +multi_image_pseudomodel(p_greens, p_reds) tuple
        +switching_model(green_model, red_model) np.ndarray
        +optical_deep_water_model(model, blue, green, vnir) np.ndarray
    }

    class reader {
        <<module>>
        +open(filename) Image
    }

    %% ── Relationships ─────────────────────────────────────────────────────
    ImageReader <|-- NetCDFReader : extends
    ImageReader <|-- GeoTIFFReader : extends

    ImageReader ..> Image : creates
    reader ..> ImageReader : delegates to
    reader ..> FILE_EXTENTIONS : uses

    LinearModel ..> ValidationSummary : creates
    bathymetry_models ..> selector : uses

    Image ..> selector : uses internally
    Image ..> SENTINEL2_BANDS : compatible with
    Image ..> MICASENSE_BANDS : compatible with
```

## Module Overview

| Module | Type | Responsibility |
|--------|------|----------------|
| `sensingpy.image` | Class | Core geospatial image container and processing |
| `sensingpy.reader` | Factory + Classes | File I/O for GeoTIFF and NetCDF formats |
| `sensingpy.masks` | Functions | Boolean array masking utilities |
| `sensingpy.selector` | Functions | Array sampling and compositing |
| `sensingpy.enums` | Enumerations | Band definitions and file extension constants |
| `sensingpy.preprocessing.deglinting` | Functions | Sun glint correction algorithms |
| `sensingpy.preprocessing.outliers` | Functions | Outlier detection and removal |
| `sensingpy.bathymetry.models` | Functions + Class | Satellite-derived bathymetry (SDB) models |
| `sensingpy.bathymetry.metrics` | Dataclass | SDB validation and error metrics |

## Key Relationships

- **`ImageReader` hierarchy**: `NetCDFReader` and `GeoTIFFReader` both implement `ImageReader.read()`, which always returns an `Image`. The `reader.open()` factory selects the correct reader based on the file extension using `FILE_EXTENTIONS`.
- **`LinearModel` + `ValidationSummary`**: `LinearModel.predict_and_evaluate()` returns a `ValidationSummary` dataclass that exposes error statistics (MAE, RMSE, MedAE, etc.) as properties.
- **`Image` internals**: The `Image` class delegates sampling operations (`interval_choice`, `sample_indices_by_interval`) to the `selector` module and supports renaming bands via `SENTINEL2_BANDS` or `MICASENSE_BANDS` enums.
- **Preprocessing independence**: `deglinting` and `outliers` operate directly on `np.ndarray`, keeping them decoupled from the `Image` class.
