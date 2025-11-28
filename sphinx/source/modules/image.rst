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

   .. rubric:: Properties

   .. autosummary::
      :nosignatures:

      band_names
      width
      height
      count
      x_res
      y_res
      transform
      xs_ys
      left
      right
      top
      bottom
      bbox
      values

   .. rubric:: Band Management

   .. autosummary::
      :nosignatures:

      select
      add_band
      drop_bands
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