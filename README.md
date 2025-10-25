# Solar-Radiation-Prediction
🌞 Solar Radiation Prediction using Machine Learning  This project focuses on predicting solar radiation intensity based on various environmental parameters such as temperature, humidity, wind speed, and wind direction. 
🌞 Solar Radiation Prediction using Machine Learning

This project focuses on predicting solar radiation intensity based on various environmental parameters such as temperature, humidity, wind speed, and wind direction. Accurate prediction of solar radiation plays a crucial role in renewable energy planning, solar panel optimization, and sustainable power generation.

🚀 Project Overview

The model uses Linear Regression to estimate solar radiation levels by analyzing weather data.
To ensure model reliability, Variance Inflation Factor (VIF) analysis was applied to detect and remove multicollinearity among features.
Model performance was evaluated using R² (Coefficient of Determination) and Mean Squared Error (MSE) metrics.

🧠 Key Concepts

Linear Regression: Establishes a linear relationship between weather variables and solar radiation.

Multicollinearity: Occurs when independent variables are highly correlated; resolved using VIF analysis.

Variance Inflation Factor (VIF): Measures how much the variance of coefficients is inflated due to multicollinearity.

R² Score: Indicates how much variation in solar radiation is explained by the model.

⚙️ Technologies Used

Python

Pandas, NumPy – Data handling and preprocessing

Scikit-learn – Machine learning model and metrics

Matplotlib, Seaborn – Data visualization

VIF Analysis – Feature selection and optimization

📊 Workflow

Data Collection – Historical weather dataset (temperature, humidity, wind data, solar radiation).

Data Preprocessing – Handling missing values, normalization, and feature selection using VIF.

Model Training – Linear Regression model fitted on processed data.

Model Evaluation – Evaluated using R², Adjusted R², and MSE metrics.

Visualization – Correlation plots and prediction vs actual comparison graphs.

📈 Results

Achieved a high R² score, indicating strong predictive performance.

Identified temperature and wind speed as the most influential factors affecting solar radiation.

🌍 Applications

Solar energy forecasting and management

Smart grid optimization

Renewable energy system design

Agricultural and environmental planning
