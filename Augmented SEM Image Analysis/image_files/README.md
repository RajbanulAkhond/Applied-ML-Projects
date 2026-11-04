# SEM Image Data and Augmentation

This directory supports the [SEM analysis project](../README.md). It contains 632 source images from three categories and three transformed copies of each image, for 2,528 image files in total.

| Source directory | Images | Related augmented directories |
| --- | --- | --- |
| `Fibres/` | 153 | `Fibres_blurred/`, `Fibres_contrast/`, `Fibres_noisy/` |
| `Films_Coated_Surface/` | 308 | `Films_Coated_Surface_blurred/`, `Films_Coated_Surface_contrast/`, `Films_Coated_Surface_noisy/` |
| `Porous_Sponge/` | 171 | `Porous_Sponge_blurred/`, `Porous_Sponge_contrast/`, `Porous_Sponge_noisy/` |

I use these matched conditions to explore how blur, contrast enhancement, and noise affect PCA, reconstruction, and clustering. Working with them gave me practice in image loading, directory-based category labels, numerical image representations, and augmentation using **Pillow** and **NumPy**.

[`augment_images.py`](augment_images.py) generates the variants with Gaussian blur (radius 15), additive Gaussian noise (standard deviation 25), and doubled contrast. The generated folders are already included. To regenerate them on another machine, first change the `base_path` inside `augment_folder` to this directory. Running the script writes into the existing augmentation folders. The script does not seed noise generation.

The source dataset link recorded in the notebook is the [B2SHARE SEM dataset](https://b2share.eudat.eu/records/19cc2afd23e34b92b36a1dfd0113a89f). Category-level and model details are in the [project README](../README.md).
