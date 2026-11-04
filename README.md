# Applied ML Projects

Three projects from my Applied Machine Learning course (P-556), exploring how machine learning can be applied to materials data and microscopy images. I worked with regression, classification, and unsupervised learning, moving from data exploration to model comparison and interpretation.

## Projects

| Project | What I set out to do | Methods I practiced |
| --- | --- | --- |
| [Material Lifespan](Material%20Lifespan/README.md) | Predict component lifespan from composition, processing conditions, structural descriptors, and defects. | Linear and polynomial regression, stochastic gradient descent, regularization, cross-validation, and residual analysis. |
| [EV Chassis Material Selection](EV%20Chassis%20Material%20Selection/README.md) | Predict the supplied material suitability label from six mechanical properties. | Logistic regression, support vector machines, random forests, hyperparameter search, voting, and stacking. |
| [Augmented SEM Image Analysis](Augmented%20SEM%20Image%20Analysis/README.md) | Examine how image transformations and feature representations affect dimensionality reduction and clustering of SEM images. | Image augmentation, PCA and reconstruction, manifold visualization, K-Means, Gaussian mixtures, and pretrained ResNet50 feature extraction. |

Each project folder contains a Jupyter notebook, a PDF export, and the associated data. The SEM project also includes an augmentation script and exported figures.

## What I learned

- **Start with the data.** I used summary statistics, distributions, correlation matrices, and scatter plots to understand feature scales, relationships, and class imbalance before fitting models.
- **Match the evaluation to the task.** I used RMSE and R² for regression, precision/recall and F1 alongside accuracy for classification, and several internal metrics plus class-label matching for clustering.
- **Compare models against a baseline.** Linear regression provided a reference for polynomial models. In the classification project, logistic regression showed how a model can achieve about 91% accuracy while failing to identify the minority class.
- **Control model complexity.** I explored regularization strengths, learning rates, polynomial degrees, and classifier hyperparameters. The unstable cubic regression experiments made numerical behavior an important part of model assessment.
- **Choose features deliberately.** I practiced scaling, categorical encoding, polynomial expansion, PCA, and transfer learning. The SEM experiments showed how much clustering can change when raw-pixel representations are replaced with pretrained image features.
- **Communicate results with evidence.** I created confusion matrices, validation curves, residual plots, image reconstructions, and comparison tables, and connected the results to the original materials questions.

## Libraries and tools I used

| Library or tool | How I used it |
| --- | --- |
| **Python and Jupyter Notebook** | Interactive analysis, experiments, explanations, and saved outputs. |
| **NumPy** | Numerical arrays, feature manipulation, noise generation, and metric calculations. |
| **pandas** | Reading CSV files, exploring datasets, grouping results, and building comparison tables. |
| **Matplotlib and seaborn** | Statistical plots, heatmaps, model comparisons, confusion matrices, and image panels. |
| **scikit-learn** | Preprocessing, data splitting, regression, classification, dimensionality reduction, clustering, model selection, and evaluation. |
| **SciPy** | Pearson correlation analysis and optimal assignment of cluster IDs to category labels. |
| **Pillow** | Loading, resizing, and transforming microscopy images. |
| **PyTorch and torchvision** | Loading an ImageNet-pretrained ResNet50 and extracting image feature vectors. |
| **umap-learn** | Optional UMAP projections for visualizing image data in two dimensions. |

## Results recorded in the notebooks

These are the saved results from the submitted notebooks; they have not been recomputed as part of preparing this repository.

| Project | Example recorded result |
| --- | --- |
| Material Lifespan | Quadratic features with L1-regularized SGD achieved test RMSE **156.16 hours** and **R² = 0.7824** on 200 test samples. |
| EV Chassis Material Selection | Random forest achieved **99.57%** test accuracy and **0.9744** F1; logistic regression achieved **91.42%** accuracy but **0** minority-class recall. |
| Augmented SEM Image Analysis | K-Means with ResNet features averaged **86.19%** label-matched agreement across four conditions, compared with **45.57%** using PCA features. These are clustering evaluations on the fitted images. |


## Getting started

From the repository root, create a Python environment and install the common dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyter numpy pandas matplotlib seaborn scipy scikit-learn
jupyter notebook
```

For the SEM notebook, also install:

```bash
python -m pip install pillow torch torchvision umap-learn
```

Open a notebook from its own project folder and run cells in order so its relative data paths resolve correctly. The PDF exports provide a convenient way to read the existing analyses without running them. These installation commands list the packages used; this repository does not provide a locked environment.

The SEM images account for most of the repository's approximately 720 MiB of project files. ResNet50 weights are downloaded by torchvision on first use, and the SEM computations can take substantially longer than the tabular examples. See each project's README for execution notes.

## Data and acknowledgments

- The EV notebook references the [Mechanical Properties of Design Materials dataset](https://www.kaggle.com/datasets/purushottamnawale/materials), described there as originating from the Autodesk Material Library. The local CSV includes the `Use` label analyzed in this project.
- The SEM notebook references this [SEM dataset record on B2SHARE](https://b2share.eudat.eu/records/19cc2afd23e34b92b36a1dfd0113a89f). This repository contains three selected categories and their augmented variants.
- The Material Lifespan notebook uses the included `Material_Lifespan_Dataset.csv`; it does not specify an original public source.
