# Principal Component Analysis (PCA) - Student Habits & Performance Analysis

This project focuses on Advanced Linear Algebraic Techniques and their application in Data Analysis, specifically Principal Component Analysis (PCA). We analyze and visualize a dataset containing student habits and performance metrics to understand the relationships between various behavioral factors and academic outcomes.

## Prerequisites

- Python 3.x
- Google Account (for Google Colab and Drive)
- Basic understanding of linear algebra concepts

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Alliance-D/PCA
cd PCA
```

2. Install required Python packages:
```bash
pip install numpy pandas matplotlib
```

## Google Drive Setup

1. Upload Dataset:
   - Sign in to your Google Drive
   - Upload `student_habits_performance.csv` to your Drive
   - Note down the path where you uploaded the file

2. Google Colab Setup:
   - Open `Template_PCA_Formative_1[Peer_23].ipynb` in Google Colab
   - Mount your Google Drive by running:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```
   - Update the file path in the notebook to match your Drive location:
     ```python
     data = pd.read_csv('/content/drive/path_to_your_file/student_habits_performance.csv')
     ``` 
     or
     ```python
     data = pd.read_csv('/content/drive/student_habits_performance.csv')
     ```

## Project Structure
```
PCA/
├── README.md
├── student_habits_performance.csv    # Dataset file
└── Template_PCA_Formative_1[Peer_23].ipynb  # Analysis notebook
```

## Core Concepts

### 1. Standardization
Implemented using NumPy, this crucial preprocessing step:
- Applies to numerical columns only
- Ensures data has mean = 0 and standard deviation = 1
- Benefits:
  - Eliminates scale bias between features
  - Enhances PCA numerical stability
  - Ensures equal feature contribution to variance
  - Critical for accurate PCA results

### 2. Covariance Matrix
A fundamental component that:
- Maps relationships between features
- Properties:
  - Diagonal elements: Feature variances
  - Off-diagonal elements: Feature covariances
- Interpretation Guide:
  - Positive covariance → Features increase together
  - Negative covariance → Inverse relationship
  - Near-zero covariance → No linear relationship
  - Symmetric matrix structure

### 3. Eigendecomposition
Core PCA computation that:
- Calculates eigenvalues and eigenvectors
- Determines principal components
- Process:
  1. Compute eigenvalues/vectors
  2. Sort by importance (eigenvalue magnitude)
  3. Select significant components
  4. Project data onto new basis

### 4. Data Visualization
Using Matplotlib to:
- Compare original vs. PCA-transformed data
- Visualize variance explained
- Plot component contributions
- Create scree plots for eigenvalue analysis

## Implementation Steps

1. Data Preparation:
   - Load the dataset
   - Handle missing values
   - Select numerical features
   - Apply standardization

2. PCA Implementation:
   - Calculate covariance matrix
   - Perform eigendecomposition
   - Sort and select components
   - Project data

3. Analysis & Visualization:
   - Create comparison plots
   - Analyze variance explained
   - Interpret results

## Libraries Used
- ![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
- ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=plastic&logo=Matplotlib&logoColor=black)

## Usage

1. Local Jupyter:
```bash
jupyter notebook Template_PCA_Formative_1[Peer_23].ipynb
```

2. Google Colab:
   - Open the notebook in Colab
   - Follow the Google Drive setup instructions above
   - Run cells sequentially

## Dataset Description

The `student_habits_performance.csv` contains:
- Student behavioral metrics
- Academic performance indicators
- Study habits data
- Performance outcomes

## Best Practices

1. Data Preprocessing:
   - Always standardize numerical features
   - Check for missing values
   - Validate data types

2. PCA Application:
   - Verify assumptions
   - Choose components wisely
   - Document variance explained

3. Result Interpretation:
   - Consider practical significance
   - Validate findings
   - Document insights

## Troubleshooting

Common issues and solutions:
1. ModuleNotFoundError:
   ```bash
   pip install <missing_module>
   ```
2. Google Drive mounting issues:
   - Ensure proper authentication
   - Check file paths
   - Verify permissions

## Notes

- Keep Jupyter kernel updated
- Document any modifications
- Save intermediate results
- Follow best practices for reproducibility
