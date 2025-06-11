# Principal Component Analysis - Student Habits & Performance

This project implements Principal Component Analysis (PCA) to analyze and visualize student habits and performance data. The analysis helps identify patterns and relationships between various student behavioral factors and their academic performance.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Alliance-D/PCA
cd PCA
```

2. Install required Python packages:
```bash
pip install numpy
pip install pandas
pip install matplotlib
```

## Project Structure
```
PCA/
├── README.md
├── student_habits_performance.csv    # Dataset file
└── Template_PCA_Formative_1[Peer_23].ipynb  # Analysis notebook
```

## Concepts

### Standardization
- Implemented using NumPy
- Applied only to numerical columns
- Ensures data has mean = 0 and standard deviation = 1
- Benefits:
  - Removes scale bias between different features
  - Enhances numerical stability for PCA
  - Ensures equal feature contribution to variance

### Covariance Matrix
- Captures relationships between features
- Square matrix properties:
  - Diagonal elements: Variance of each feature
  - Off-diagonal elements: Covariance between features
- Interpretation:
  - Positive covariance: Features increase together
  - Negative covariance: One feature increases while other decreases
  - Zero covariance: No linear relationship

### Eigendecomposition
- Computes eigenvalues and eigenvectors of covariance matrix
- Sorts components by importance
- Selects principal components
- Projects original data onto new dimensions

### Data Visualization
- Uses Matplotlib to visualize:
  - Original data distribution
  - Transformed data after PCA

## Libraries Used
- ![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
- ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=plastic&logo=Matplotlib&logoColor=black)

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook Template_PCA_Formative_1[Peer_23].ipynb
```

2. Follow the step-by-step analysis:
   - Data loading and standardization
   - Covariance matrix calculation
   - Eigendecomposition
   - Principal component selection
   - Data projection and visualization

## Dataset

The `student_habits_performance.csv` file contains various metrics about student habits and their corresponding academic performance. The PCA analysis helps identify the most significant factors affecting student performance.

## Notes

- Make sure all required packages are installed before running the notebook
- The notebook includes detailed comments explaining each step of the PCA process
- Visualizations help understand the data transformation and dimensionality reduction
