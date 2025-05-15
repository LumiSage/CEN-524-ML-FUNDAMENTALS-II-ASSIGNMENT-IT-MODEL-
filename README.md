
# CEN523 Assignment Report by** OYEBOWALE EMMANUEL 20CJ027487**

## A. Problem Background

During my 400-level IT, I served as a DevOps Engineer at **Conclase Consulting**s where I worked with developers to manage version control, deploy code to cloud platforms, implement CI/CD pipelines, and monitor running applications.

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

MSE on Test Set: 61.7816584405222

**QUESTIONS AND ANSWERS**

1. How does normalization affect the feature values?

 ANS: Normalization with zero mean and unit variance ensures all features contribute equally to training. It speeds up convergence in gradient descent and prevents scale-dominant features.

2. Why does MSE penalize large errors more than MAE?

 ANS: MSE squares the errors, making large differences more impactful, while MAE treats all errors linearly.

3. A small learning rate converges slowly; a large one may overshoot or diverge. The chosen rate (0.01) balanced speed and stability.

 ANS: Why might the model perform differently on real vs. synthetic data?**  
  Synthetic data is often cleaner and follows known relationships. Real-world data contains noise, outliers, and hidden variables.

4. Improvement Suggestion:**  
 ANS: Implement mini-batch gradient descent or add L2 regularization to avoid overfitting.

**Key findings:**

Normalization improved convergence speed.

The final MSE and MAE for the real-world dataset were significantly higher than for synthetic data, reflecting the noise and complexity of Shell’s IT systems.

A smaller learning rate gave smoother convergence, while larger ones risked divergence.

scikit-learn’s model reached better performance in fewer iterations, but gradient descent offered more transparency and control.

Improvement Suggestion: Implement adaptive learning rates (e.g., Adam or RMSProp) to stabilize training and converge faster, especially on multi-feature datasets like asset logs and configuration records in Shell systems.

---

**Author**: Emmanuel  
**Course**: CEN523  
**Date**: May 2025
