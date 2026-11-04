# EV Chassis Material Selection

## What I am trying to do

I compare classification methods for predicting the supplied `Use` label, treated in this project as an indication of material suitability for an electric-vehicle chassis. I want to understand which models capture the relationships between mechanical properties and that label, and whether combining classifiers improves the results.

## Dataset

[`material.csv`](material.csv) contains **1,552 material records**, a material identifier, six numerical inputs, and the binary target `Use`.

| Input | Property | Unit given in the notebook |
| --- | --- | --- |
| `Su` | Ultimate tensile strength | MPa |
| `Sy` | Yield strength | MPa |
| `E` | Elastic modulus | MPa |
| `G` | Shear modulus | MPa |
| `mu` | Poisson's ratio | Dimensionless |
| `Ro` | Density | kg/m³ |

`Material` identifies each entry and is excluded from the model inputs. The target is imbalanced: **135 `True`** records and **1,417 `False`** records, so only about 8.7% belong to the positive class.

The notebook references the [Mechanical Properties of Design Materials dataset on Kaggle](https://www.kaggle.com/datasets/purushottamnawale/materials) and describes the mechanical-property data as originating from the Autodesk Material Library. The notebook does not establish how the local `Use` labels were assigned. This analysis evaluates prediction of those labels; their engineering meaning would need independent validation before using a model for chassis design.

## What I implemented

1. Examined distributions, skewness, outliers, and correlations between mechanical properties and the target.
2. Created stratified training, validation, and test partitions in approximately 70/15/15 proportions: 1,086, 233, and 233 records.
3. Fitted `StandardScaler` on the training partition and applied the same transformation to the validation and test partitions.
4. Used five-fold `GridSearchCV` to tune logistic regression, kernel support vector machines, and random forests.
5. Compared accuracy, positive-class precision, recall, F1, and confusion matrices across the three partitions.
6. Investigated random-forest feature importance and compared hard voting, validation-weighted soft voting, and stacking with a logistic-regression final estimator.

## Results recorded in the notebook

| Model | Test accuracy | Positive-class F1 |
| --- | --- | --- |
| Logistic regression | 91.42% | 0.0000 |
| Support vector machine | 99.14% | 0.9500 |
| Random forest | 99.57% | 0.9744 |
| Hard voting | 99.57% | 0.9744 |
| Soft voting | 99.57% | 0.9744 |
| Stacking | 99.14% | 0.9500 |

The most useful lesson was that accuracy alone can be misleading: logistic regression achieved about 91% accuracy while its recall for the positive class was zero. The best individual model, random forest, identified 19 of the 20 positive test examples and made no positive predictions among the 213 negative examples. Voting matched its scores on this split; stacking did not improve them.

These are saved notebook results and have not been recomputed for this repository. Scaling happens before the internal grid-search folds, so fold validation data influence the scaling statistics. Moving scaling into a `Pipeline` would improve the separation within cross-validation. The outer validation and test partitions use training-fitted scaling. A separate dataset would also be needed to assess transfer beyond this collection of materials.

## Skills I developed

- Translating a materials question into a supervised classification experiment.
- Recognizing class imbalance and checking minority-class precision, recall, and F1.
- Using stratified splits and training-fitted feature standardization.
- Comparing linear, kernel-based, and tree-based decision models.
- Tuning model hyperparameters and reading cross-validation results.
- Building voting and stacking ensembles, and checking whether they add value over an individual model.
- Using confusion matrices and feature importance to explain model behavior.

## Libraries I used

**pandas**, **NumPy**, **Matplotlib**, **seaborn**, and **scikit-learn**, in a **Jupyter notebook**. The main model-selection and ensemble tools include `GridSearchCV`, `LogisticRegression`, `SVC`, `RandomForestClassifier`, `VotingClassifier`, and `StackingClassifier`.

## Files and how to run

- [`EV_chassis_classification.ipynb`](EV_chassis_classification.ipynb): analysis, model tuning, and saved outputs.
- [`EV_chassis_classification.pdf`](EV_chassis_classification.pdf): PDF export of the analysis.
- [`material.csv`](material.csv): input data with the supplied labels.

Install the common dependencies listed in the [repository README](../README.md#getting-started), then launch Jupyter from this directory:

```bash
cd "EV Chassis Material Selection"
jupyter notebook EV_chassis_classification.ipynb
```

Run the cells in order. The grid searches fit many configurations and can take time. Some existing stacking print statements call the final estimator “Ridge”; the implemented `final_estimator` is `LogisticRegression`.
