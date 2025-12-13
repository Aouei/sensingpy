Image Module
============

The Image module provides functionality for handling geospatial image data through the Image class.

Image Class
-----------

.. autoclass:: sensingpy.image.Image
   :members:
   :undoc-members:
   :show-inheritance:
   :member-order: groupwise

   .. note::
      
      **In-place Operations**
      
      Most methods in the Image class support an ``inplace`` parameter (default ``True``) 
      that controls whether operations modify the image in-place or return a modified copy:
      
      - ``inplace=True`` (default): Modifies the image in-place and returns self for method chaining
      - ``inplace=False``: Returns a new Image instance without modifying the original
      
      Example::
      
         # In-place operations (default behavior)
         image.mask(water_mask).reproject(new_crs).dropna()
         
         # Non-mutating operations (create copies)
         masked = image.mask(water_mask, inplace=False)
         reprojected = image.reproject(new_crs, inplace=False)

   .. rubric:: Properties

   .. autosummary::
      :nosignatures:

      band_names
      width
      height
      count
      x_res
      y_res
      res
      transform
      xs_ys
      left
      right
      top
      bottom
      bbox
      values
      attrs
      attrs_keys
      attrs_values

   .. rubric:: Band Management

   .. autosummary::
      :nosignatures:

      select
      add_band
      drop_bands
      keep_bands
      replace
      rename
      rename_by_enum

   .. rubric:: Spatial Operations

   .. autosummary::
      :nosignatures:

      reproject
      align
      resample
      clip
      merge

   .. rubric:: Masking and Filtering

   .. autosummary::
      :nosignatures:

      mask
      geometry_mask
      dropna

   .. rubric:: Data Analysis

   .. autosummary::
      :nosignatures:

      normalized_diference
      extract_values
      interval_choice
      sample_indices_by_interval

   .. rubric:: Data Export

   .. autosummary::
      :nosignatures:

      to_netcdf
      to_tif

   .. rubric:: Utility Methods

   .. autosummary::
      :nosignatures:

      empty_like
      copy

Module Functions
----------------

.. autofunction:: sensingpy.image.compose