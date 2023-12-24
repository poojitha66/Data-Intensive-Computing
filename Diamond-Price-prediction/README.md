### Diamond Price Prediction

#### Problem Statement
The diamond market lacks precision in pricing, leading to inefficiencies. Our goal is to predict diamond prices accurately based on attributes like cut, color, clarity, carat, table, x, y, and z to address this inconsistency.

#### Background
Assessing diamond attributes is subjective, creating challenges in evaluation. Consumers lack comprehensive education, relying on retailer-provided data, which might not be impartial. Accurate pricing benefits both buyers and sellers.

#### Importance of the Problem
Developing a robust machine-learning model aids data-driven decision-making in diamond pricing. Our model considers multiple attributes, reducing reliance on subjective information.

---

### Deployment

#### Description
We've built a web application for diamond price prediction. This user-friendly interface simplifies the prediction process, allowing users to input various factors and estimate diamond prices accurately.

#### Technology Used
- **Web Framework:** Flask
- **Front-end:** HTML, CSS
- **Back-end:** Python (Flask)
- **Machine Learning Techniques:** Linear Regression, Lasso Regression, Ridge Regression, Decision Tree models

---

### Diamonds

#### Dataset Overview
The dataset contains nearly 54,000 diamonds with attributes like price, carat weight, cut quality, color, clarity, and dimensional features (x, y, z). 

#### Machine Learning
We've explored regression and classification techniques on this dataset.

#### Regression Algorithms
We've tested various regression algorithms, such as Lasso Regression, Linear Regression, Ridge Regression, AdaBoost, XGBRFRegressor, Decision Tree, Gradient Boosting, Bagging, Random Forest, and Extra Trees. Among these, the Extra Trees Regressor provided the highest accuracy at 98.16%.

#### Classification Algorithms
For classification, we employed kNN, SVM, and Logistic Regression. SVM produced the best accuracy at 75.27%.

---

### Summary
Our project aims to enhance diamond pricing accuracy using machine learning models. The web app simplifies price prediction for users based on multiple diamond attributes. By utilizing regression and classification techniques, we achieved significant accuracy, especially with algorithms like Extra Trees Regressor and SVM.
