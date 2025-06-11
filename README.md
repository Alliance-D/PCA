Principle Component Analysis
This assignment focuses on Advanced Linear Algebraic Techniques and their application in Data Analysis. In this assignment, we focused on Principal Component Analysis in analyzing and visualizing datasets, specifically: "C:\Users\Administrator\PCA\fuel_econ (1).csv", that explores fuel consumption in different cars, what influences consumption and the various factors arising from that such as CO2 emission.

Concepts
Standardization
This is done using numpy. Standardization is done on the numerical columns only. It aims to ensure the data has a mean of 0 and a standard deviation of 1. Standardization accomplishes the following:

1. Removes bias from different scales making sure that none dominates the other. For example in our case, since we had different scales for different columns, it proves significant.

2. For algorithms such as PCA, which assume a zero mean distribution, it enhances numerical stability.

3. It ensures the features contribute equally to the variance.
Covariance Matrix
Captures the relationship between the various features i.e how they vary in relation to each other For a dataset with multiple features, the covariance matrix generalizes this concept. It is a square matrix where:

-Diagonal elements represent the variance of each feature.

-Off-diagonal elements represent the covariance between features.
If covariance is positive, both variables increase together.

If covariance is negative, one variable increases while the other decreases.

If covariance is close to zero, no linear relationship.

Eigendecomposition
This entails finding the eigenvalues and eigenvectors of the covariance matrix, sorting them to understand their importance to your analysis, selecting the columns derived from PCA and projecting them to the original dataset.

Data Visualization
We then utilize matplotlib to visualize the data before PCA and after.
