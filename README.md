# Iris Species Classification

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/Model-Decision%20Tree-F7931E?style=flat)](https://scikit-learn.org/)
[![Dataset](https://img.shields.io/badge/Dataset-Iris-4C78A8?style=flat)](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
[![Notebook](https://img.shields.io/badge/Notebook-Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)](#)

## Overview

This repository contains a machine learning portfolio project for multiclass classification on the classic **Iris** dataset. The goal is to classify Iris flowers as Setosa, Versicolor, or Virginica using a transparent Decision Tree workflow.

The project emphasizes exploratory data analysis, reproducible validation, interpretable modeling, and careful diagnostic interpretation. The Decision Tree is trained with the entropy criterion, then inspected through tree structure, decision paths, leaf nodes, feature importance, permutation importance, pruning diagnostics, confusion matrix, and entropy analysis.

The value of this project is not in solving a difficult benchmark. Iris is intentionally simple and well known. The value is in demonstrating a clean machine learning workflow, disciplined validation, model interpretability, and cautious interpretation of results.

## Project Objective

The objective is to build a supervised multiclass classification workflow that predicts the `target` species label:

- `0`: Setosa
- `1`: Versicolor
- `2`: Virginica

The project demonstrates the following technical components:

- Data quality checks for missing values, duplicated rows, data types, and class balance
- Exploratory Data Analysis (EDA)
- Visual comparison of feature distributions by species
- Pairwise feature relationship analysis
- Correlation analysis with appropriate caution for encoded class labels
- Exploratory t-SNE visualization
- Stratified train/test split
- Stratified cross-validation
- Decision Tree classification using entropy
- Classification report and confusion matrix
- Impurity-based feature importance
- Permutation importance as a complementary diagnostic
- Cost-complexity pruning analysis with cross-validation
- Decision path and leaf-node diagnostics
- Misclassified sample inspection
- Node depth and entropy-based interpretability

## Dataset

The data comes from the Iris dataset bundled with scikit-learn through `sklearn.datasets.load_iris`. No external data download is required.

| Property | Description |
| --- | --- |
| Observations | 150 flower samples |
| Classes | 3 balanced species classes |
| Features | 4 numerical measurements in centimeters |
| Target | Encoded species label |

| Feature | Description |
| --- | --- |
| `sepal length (cm)` | Sepal length measurement |
| `sepal width (cm)` | Sepal width measurement |
| `petal length (cm)` | Petal length measurement |
| `petal width (cm)` | Petal width measurement |

## Repository Structure

```text
iris-prediction/
|-- iris-decision-tree-eda-interpretability.ipynb        # Main analysis and modeling notebook
|-- requirements.txt                  # Python dependencies
|-- make_env.py                       # Optional environment setup helper
|-- .gitignore
`-- README.md
```

The local file `arvore_decisao_iris_giovanni_2025_05_03.pdf` is a generated tree artifact and is not required to reproduce the notebook.

## Methodology

### 1. Data Quality Checks

The notebook verifies basic data quality before exploratory analysis and modeling.

Checks include:

- Missing values by column
- Duplicated rows
- Column data types
- Class distribution

The Iris dataset is clean and balanced, but this step is included because data validation is part of a professional machine learning workflow. Duplicate measurement rows are reviewed rather than automatically removed, since repeated flowers can legitimately share the same recorded values.

### 2. Exploratory Data Analysis

The notebook inspects dataset shape, descriptive statistics, univariate distributions, bivariate relationships, correlations, and a t-SNE projection.

Key descriptive observations include:

- Setosa is clearly separated from the other species by petal length and petal width.
- Versicolor and Virginica overlap more substantially, especially in sepal measurements.
- Petal length and petal width are strongly related and provide the clearest visual class separation.
- Correlations with the encoded target are treated only as exploratory context because the target is categorical.
- t-SNE is used as an exploratory visualization, not as model validation.

### 3. Reproducibility and Data Handling

The notebook defines shared constants for the random seed, test size, number of cross-validation folds, and permutation-importance repetitions. The train/test split uses stratification to preserve class balance across partitions.

The original DataFrame is kept intact during analysis. Plotting and modeling cells use copied feature matrices or plotting-specific DataFrames when additional helper columns are needed.

### 4. Modeling

The main model is `DecisionTreeClassifier` from scikit-learn.

| Model Setting | Value |
| --- | --- |
| Model family | Decision Tree |
| Criterion | Entropy |
| Main task | Multiclass classification |
| Random state | Fixed for reproducibility |

The Decision Tree is intentionally retained as the main model because the project focuses on interpretability and model diagnostics rather than maximizing performance with a more complex algorithm.

### 5. Validation

The notebook separates validation signals into complementary views:

| Evaluation | Purpose | Interpretation |
| --- | --- | --- |
| Stratified holdout validation | Evaluates the fitted tree on a fixed test split. | Useful first estimate, but sensitive to one small split. |
| Stratified cross-validation | Checks performance stability across multiple folds. | Better summary for a small balanced dataset. |
| Classification report | Shows precision, recall, and F1-score by species. | Helps identify class-specific performance. |
| Confusion matrix | Shows exact error patterns on the holdout test set. | Expected errors occur mainly between Versicolor and Virginica. |
| Decision-path accuracy check | Confirms that path-level diagnostics match the holdout predictions. | Links aggregate performance to individual sample routing. |

The notebook avoids overclaiming based on one split because the Iris dataset is small.

### 6. Feature Importance and Model Complexity

The notebook includes two feature-importance diagnostics:

- Impurity-based Decision Tree feature importance
- Permutation importance on the holdout set

Impurity-based importance summarizes how much each feature contributes to reducing impurity across the fitted tree. Permutation importance measures how much holdout accuracy changes when a feature is randomly shuffled.

Both methods are interpreted cautiously. Petal length and petal width are strongly correlated, so importance values should be treated as model-specific diagnostic evidence rather than causal or universal feature importance.

The notebook also includes a cost-complexity pruning analysis using `ccp_alpha`. Candidate pruning values are compared with stratified cross-validation on the training partition. The purpose is methodological maturity: pruning is evaluated as a model-complexity check, not forced as an improvement.

### 7. Interpretability and Diagnostics

The notebook includes several Decision Tree diagnostics:

- Tree visualization
- Internal node depth inspection
- Correctly classified sample inspection
- Decision paths for all test observations
- Misclassified sample inspection
- Root and child-node entropy analysis
- Entropy summary for every tree node
- Entropy-by-node visualization

Internal nodes are labeled by `majority_class`, while leaf nodes represent terminal predictions. This distinction is important because internal nodes describe intermediate sample composition, not final classifications.

Entropy is interpreted together with node sample counts. High entropy in a very small node is treated as evidence of a local borderline region, not a broad general pattern.

## Reported Results

The notebook is designed to compute results during execution. With the current Decision Tree workflow, the holdout accuracy is approximately:

| Metric / Evaluation | Reported Value | Notes |
| --- | ---: | --- |
| Holdout accuracy | `~0.93` | Stratified 20% test split with fixed random state. |
| Main error pattern | Versicolor vs. Virginica | Consistent with EDA overlap. |
| Setosa performance | Near-perfect / perfect on the holdout split | Consistent with clear petal-based separation. |

Cross-validation scores, pruning diagnostics, impurity-based feature importance, and permutation importance are generated in the notebook and should be interpreted together rather than as interchangeable metrics.

## How to Reproduce

### 1. Clone the repository

```bash
git clone https://github.com/Giovannipersio/iris-prediction.git
cd iris-prediction
```

### 2. Create and install the environment

You can use the helper script:

```bash
python make_env.py
```

Or create the environment manually:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

Open and execute:

```text
iris-decision-tree-eda-interpretability.ipynb
```

The notebook will run data quality checks, EDA, Decision Tree training, validation, confusion matrix, feature importance diagnostics, pruning analysis, decision-path diagnostics, misclassified sample inspection, and entropy analysis.

## Requirements

Main libraries used in this project:

| Library | Purpose |
| --- | --- |
| `numpy`, `pandas` | Data manipulation |
| `matplotlib`, `seaborn` | Visualization |
| `scipy` | Entropy support |
| `scikit-learn` | Dataset loading, splitting, modeling, validation, inspection, pruning, and metrics |
| `ipykernel`, `jupyterlab` | Notebook execution environment |

See `requirements.txt` for dependency version constraints.

## Limitations

This project has the following limitations:

- The Iris dataset is small, clean, balanced, and well known, so results should not be generalized to harder real-world classification settings.
- The Decision Tree is the only main model family evaluated.
- t-SNE is exploratory and does not validate model performance.
- Feature importance and permutation importance explain fitted model behavior, but do not establish causality.
- Correlated predictors, especially petal length and petal width, can affect how importance is distributed.
- Deeper branches near the Versicolor-Virginica boundary may reflect local training-set structure.
- Pruning is evaluated as a complexity diagnostic, not as proof that a simpler tree is always better.

## Next Steps

Potential extensions include:

- Run repeated cross-validation for a more stable performance estimate.
- Compare the selected tree against simple baseline models such as logistic regression or k-nearest neighbors.
- Add a controlled ablation study to quantify the effect of petal and sepal features separately.
- Export regenerated figures to a structured `outputs/` directory.
- Save a clean executed notebook after installing dependencies in a reproducible environment.
- Add a fully pinned lock file for exact environment reproduction.

## Author

Developed by **Giovanni Persio**.

This project is part of a data science portfolio focused on interpretable machine learning, validation methodology, and model diagnostics.
