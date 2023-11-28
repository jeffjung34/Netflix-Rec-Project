# Netflix-Recommendation Project Description

Getting Started
Step 1: Installation
Before running the project, ensure that all necessary dependencies are installed. You can do this by installing the following Python libraries: pandas, numpy, scipy, matplotlib, seaborn

Step 2: Setting Up Git Large File Storage (LFS)
Since this project uses Git LFS to handle large files, after cloning the project, you need to set up Git LFS:
git lfs install
git lfs pull

Step 3: Project Structure
The project consists of three main Jupyter Notebook files:

generateMatrix.ipynb: This file contains the bulk of the logic, including the creation of the user-rating matrix and various tests conducted on it.

runMatrixFactorization.ipynb: This file focuses on applying more complex and optimal matrix operations (such as Singular Value Decomposition - SVD) for generating user recommendations.

efficient.ipynb: An efficient implementation of the matrix factorization processes detailed in runMatrixFactorization.ipynb, optimized for performance.

Usage
To use this project, run each Jupyter Notebook in the order listed above. Each notebook contains detailed instructions and comments to guide you through the process.
