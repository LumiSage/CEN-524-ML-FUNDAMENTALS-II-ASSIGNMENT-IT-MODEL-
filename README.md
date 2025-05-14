
# CEN523 Assignment Report

## A. Problem Background

During my 400-level IT, I served as a DevOps Engineer where I worked with developers to manage version control, deploy code to cloud platforms, implement CI/CD pipelines, and monitor running applications.

For this assignment, I modeled the task of **monitoring system reliability** based on:
- Deployment frequency
- Number of CI/CD failures

## 1. Generated Synthetic Data

The dataset includes:
- **Deployment_Frequency** (input): How many times code is deployed per week.
- **CI_CD_Failures** (input): Number of failures in CI/CD pipelines weekly.
- **System_Reliability_Score** (output): Derived based on how frequent and smooth deployments are. Score is between 0–100.

## 2. Design Matrix Construction

A design matrix was built with an intercept term and the normalized feature values. Normalization ensures all input features contribute equally during training.

## 3. Preprocessing

Min-Max Normalization was applied to bring feature values to the [0, 1] range.

### ➕ Normalization Effect

Normalization ensures:
- Faster convergence in gradient descent.
- Prevents features with larger scales from dominating model learning.

## 4. Cost Function and Gradient Descent

- Implemented Mean Squared Error (MSE) as the cost function.
- Used batch gradient descent to update weights iteratively.

## 5. Model Testing

The model was evaluated using MSE on a held-out test set.

## 📁 Files in Repository

- `devops_synthetic_data.csv`: Synthetic dataset used
- `model.py`: Python code for preprocessing, training, and evaluation
- `README.md`: This report

---

**Author**: Emmanuel  
**Course**: CEN523  
**Date**: May 2025
