# Augmented SEM Image Analysis

## What I am trying to do

I investigate how image augmentation and feature representation change the structure that unsupervised learning methods find in scanning electron microscopy (SEM) images. I compare original images with blurred, contrast-enhanced, and noisy variants, then examine dimensionality reduction, reconstruction, and clustering.

## Dataset

The notebook references this [SEM dataset record on B2SHARE](https://b2share.eudat.eu/records/19cc2afd23e34b92b36a1dfd0113a89f). The local subset contains three categories:

| Category | Original images | Images per augmented condition |
| --- | --- | --- |
| Fibres | 153 | 153 |
| Films / coated surfaces | 308 | 308 |
| Porous / sponge structures | 171 | 171 |
| **Total** | **632** | **632** |

There are **2,528 image files** across the original and three augmented conditions. Augmented copies are transformations of the same source images. The directory names supply the category labels used to color projections and evaluate clustering.

For pixel-based analysis, images are converted to grayscale, resized to **256 × 256**, flattened into 65,536 features, and standardized. The ResNet branch instead uses RGB images resized to **224 × 224** with ImageNet normalization.

## What I implemented

1. Loaded images from the category/condition directories and compared their dimensionality using PCA and a 95% explained-variance threshold.
2. Reconstructed selected images from PCA coordinates and evaluated reconstruction with MSE and PSNR.
3. Compared two-dimensional PCA, t-SNE, locally linear embedding (LLE), and optional UMAP projections. The nonlinear projections use subsets of up to 300 images per condition.
4. Used K-Means with PCA features, exploring inertia, silhouette, Davies–Bouldin, and Calinski–Harabasz scores for different cluster counts.
5. Extracted 2,048-dimensional feature vectors from an ImageNet-pretrained ResNet50 and repeated K-Means clustering without fine-tuning the network.
6. Fitted Gaussian mixture models through expectation-maximization, compared cluster counts using AIC, BIC, and silhouette scores, and sampled models in PCA space to visualize generated patterns.
7. Compared three-cluster assignments with the known category labels using optimal cluster-label matching and confusion matrices.

The augmentation helper applies Gaussian blur with radius 15, Gaussian white noise with standard deviation 25, and contrast enhancement by a factor of 2.

## Results recorded in the notebook

| Condition | PCA components for approximately 95% variance | K-Means + PCA agreement | K-Means + ResNet agreement |
| --- | --- | --- | --- |
| Original | 294 | 43.83% | 86.08% |
| Blurred | 75 | 43.51% | 86.39% |
| Contrast-enhanced | 359 | 50.95% | 87.34% |
| Noisy | 304 | 43.99% | 84.97% |

Across the four conditions, mean label-matched agreement was **45.57%** for K-Means with PCA features and **86.19%** with ResNet features. Gaussian mixtures with ResNet features averaged **86.27%** agreement.

These results made feature representation a central lesson: preserving pixel variance and separating morphology categories are different objectives. Blur also reduced the number of PCA components needed for the variance threshold in this experiment.

These are saved outputs and have not been recomputed for this repository. Cluster-label agreement is evaluated on the same images used to fit the clustering models, after matching cluster IDs to known labels. It is not a held-out classification score. Generated images are samples from fitted models; their appearance does not establish physically realistic microstructure. The generation cell inverts PCA but does not undo the preceding standardization, so its output is not a calibrated original-intensity image.

## Skills I developed

- Organizing image data and applying controlled transformations with Pillow and NumPy.
- Preparing image matrices for dimensionality reduction and measuring reconstruction error.
- Comparing linear and nonlinear embeddings while recognizing that a 2D projection shows only part of the data structure.
- Selecting and evaluating cluster counts with multiple metrics.
- Using pretrained neural networks as feature extractors through PyTorch and torchvision.
- Comparing distance-based clustering with probabilistic mixture models.
- Matching arbitrary cluster IDs to category labels and interpreting confusion matrices.

## Libraries I used

**NumPy**, **pandas**, **Matplotlib**, **seaborn**, **Pillow**, **scikit-learn**, **SciPy**, **PyTorch**, **torchvision**, and optionally **umap-learn**, in a **Jupyter notebook**.

## Files and how to run

- [`SEMimage.ipynb`](SEMimage.ipynb): analysis and saved experimental outputs.
- [`SEMimage.pdf`](SEMimage.pdf): PDF export of the analysis.
- [`image_files/`](image_files/README.md): source images, augmented variants, and `augment_images.py`.
- [`original_vs_reconstructed.png`](original_vs_reconstructed.png): saved reconstruction panel.
- [`q5c_generated_images_em.png`](q5c_generated_images_em.png): saved Gaussian-mixture sampling panel.

Install the common dependencies and SEM-specific packages listed in the [repository README](../README.md#getting-started), then run:

```bash
cd "Augmented SEM Image Analysis"
jupyter notebook SEMimage.ipynb
```

Run cells in order. The augmented images are already included, so regeneration is optional. The augmentation script currently uses an absolute `base_path` inside `augment_folder`; point it at this project's `image_files` directory before using the helper on another machine. Its random noise generation is not seeded, so regenerated noisy images will differ unless a seed is added.

The notebook uses CUDA when available and otherwise runs feature extraction on the CPU. torchvision downloads the pretrained weights on first use. The image arrays and repeated PCA, mixture-model, and feature-extraction steps can require substantial memory and compute time. Image loading follows filesystem order, so exact sampled images may vary between machines even where a random seed is set.

The notebook acknowledges GitHub Copilot assistance during coding.
