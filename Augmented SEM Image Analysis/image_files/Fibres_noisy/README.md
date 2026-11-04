# Fibres: Noisy Images

This folder contains **153 images** for the **Fibres** category in the [SEM image analysis project](../../README.md).

These copies add zero-mean Gaussian noise with standard deviation 25, clipping pixel values to the range 0–255. I use them to explore how added noise affects dimensionality reduction and clustering.

I practiced generating random noise with NumPy, manipulating image arrays, and comparing model behavior under image perturbations.

See the [image-data README](../README.md) for the source dataset, augmentation script, and full directory structure. The project notebook uses the image files in this folder; this README is ignored by its image loader.
