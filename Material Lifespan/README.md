# Material Lifespan Prediction

## What I am trying to do

I explore whether material composition, manufacturing conditions, structural descriptors, and defect counts can predict component lifespan. The target is `PredictedHours`, and the central comparison is whether polynomial features improve on a linear regression baseline.

## Dataset

[`Material_Lifespan_Dataset.csv`](Material_Lifespan_Dataset.csv) contains **1,000 rows** with **15 input attributes** and one target:

- **Composition:** nickel, iron, cobalt, and chromium composition.
- **Processing:** cooling rate, quench duration, forge duration, and heat-processing time.
- **Defects:** minor, major, and edge defect counts.
- **Categorical descriptors:** component type, structure type, initial position, and formation method.
- **Target:** `PredictedHours`, expressed in hours.

The notebook splits the data into 800 training and 200 test samples, stratified by component type. The original public source of this CSV is not specified in the notebook.

## What I implemented

1. Explored distributions, summary statistics, and Pearson correlations, including relationships between inputs and the lifespan target.
2. Standardized numerical attributes and one-hot encoded the categorical attributes using a `ColumnTransformer`, producing 19 model inputs.
3. Compared ordinary least-squares linear regression with `SGDRegressor` using four-fold cross-validation and RMSE.
4. Tested L2, L1, and elastic-net penalties, along with changes to learning rate and the elastic-net mixing parameter.
5. Expanded the inputs to degree-two and degree-three polynomial features, inspected training/validation curves, and compared regularization settings.
6. Fitted the selected configuration on the full training set, evaluated the test set, and plotted predictions, residuals, and model coefficients.

The notebook's labels “Ridge,” “Lasso,” and “Elastic Net” refer to the corresponding penalties applied through `SGDRegressor` in these comparisons.

## Results recorded in the notebook

| Experiment or metric | Saved result |
| --- | --- |
| Linear regression, mean four-fold CV RMSE | 313.70 hours |
| Selected model | Degree-two polynomial features with L1-regularized SGD, `alpha=1.0` |
| Number of expanded features | 209 |
| Selected model, mean four-fold CV RMSE | 160.06 ± 4.39 hours |
| Test RMSE | 156.16 hours |
| Test R² | 0.7824 |
| Test MAE | 130.56 hours |

The quadratic model improved the recorded prediction errors substantially. Cubic expansion produced 1,539 features and severe numerical instability in the SGD experiments. These outputs illustrate why additional model complexity needs both validation and convergence checks.

These numbers come from saved notebook outputs and have not been recomputed for this repository. Preprocessing and polynomial scaling are fitted before cross-validation, so the reported CV estimates include information from the validation folds. A stricter follow-up would fit these transformations inside each fold using a `Pipeline`. The outer test split is transformed using training-fitted preprocessing.

## Skills I developed

- Preparing mixed numerical and categorical data for regression.
- Comparing least-squares and iterative optimization approaches using a common error metric.
- Understanding how L1, L2, and elastic-net penalties affect model fitting.
- Building polynomial features and diagnosing unstable optimization as feature counts grow.
- Reading learning curves and residual plots rather than relying on a single score.
- Interpreting model coefficients as dataset associations, with attention to feature scaling and correlated inputs.

## Libraries I used

**pandas**, **NumPy**, **Matplotlib**, **seaborn**, **SciPy**, and **scikit-learn**, in a **Jupyter notebook**. Key scikit-learn tools include `ColumnTransformer`, `StandardScaler`, `OneHotEncoder`, `PolynomialFeatures`, `LinearRegression`, `SGDRegressor`, `KFold`, and regression metrics.

## Files and how to run

- [`H1_Q2_Material_Lifespan.ipynb`](H1_Q2_Material_Lifespan.ipynb): analysis, experiments, and saved outputs.
- [`H1_Q2_Material_Lifespan.pdf`](H1_Q2_Material_Lifespan.pdf): PDF export of the analysis.
- [`Material_Lifespan_Dataset.csv`](Material_Lifespan_Dataset.csv): input data.

Install the common dependencies listed in the [repository README](../README.md#getting-started), then launch Jupyter from this directory:

```bash
cd "Material Lifespan"
jupyter notebook H1_Q2_Material_Lifespan.ipynb
```

Run the cells in order. The final optional feature-name inspection cell references `poly_feat`, which is not defined by the preceding cells. To run that inspection after fitting the selected quadratic model, replace `poly_feat.get_feature_names_out(input_feature_names)` with `poly_features_final.get_feature_names_out(input_feature_names)`. The prediction and evaluation cells appear before this inspection.

The notebook acknowledges GitHub Copilot assistance during coding.
