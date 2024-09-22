import streamlit as st

st.title('About the Laptop Price Predictor Project')

st.write("""
This project is a Machine Learning-based laptop price predictor. It aims to predict the price of laptops based on various features such as brand, type, CPU frequency, RAM, GPU, screen resolution, and storage options. The data for this project was sourced from Kaggle, and multiple machine learning models were tested to find the best-performing one.

### Key Features:
- **Brand:** The manufacturer of the laptop (e.g., Dell, Apple, HP).
- **Type:** The category of the laptop (e.g., Ultrabook, Gaming).
- **CPU Frequency:** The clock speed of the laptop's processor.
- **RAM:** The size of the RAM in gigabytes.
- **GPU Company:** The company that makes the laptop's graphics card.
- **Weight:** The weight of the laptop.
- **CPU Company:** The manufacturer of the CPU.
- **IPS Panel:** Whether the laptop has an IPS display.
- **Screen Size:** The diagonal size of the screen.
- **Screen Resolution:** The pixel resolution of the screen.
- **SSD/HDD/Hybrid/Flash Storage:** The various types of storage sizes available.
- **Operating System:** The OS that the laptop runs on (e.g., Windows, MacOS).

### Methodology:
The project uses a dataset from Kaggle, which contains information on various laptops and their prices. The Random Forest Regressor model was chosen for deployment as it achieved the best performance with an **88% R² score**.

Several other models like Linear Regression, Decision Trees, and Gradient Boosting were tested during the development phase. Random Forest emerged as the best due to its ability to handle non-linear relationships and interactions between the features effectively.

### Why Random Forest?
Random Forest is an ensemble learning method that combines multiple decision trees to improve prediction accuracy. It works by averaging the predictions of individual trees, reducing the likelihood of overfitting and producing better generalization.

### Results:
The model was trained on a significant number of data points, achieving a high accuracy with an R² score of 88%. This means that the model can explain 88% of the variance in laptop prices based on the input features.

### Future Scope:
There is potential to further improve the model by incorporating more recent datasets, expanding feature engineering, and experimenting with deep learning techniques to improve the predictive performance.

This project is part of the broader goal of exploring machine learning techniques and their applications in pricing prediction problems.
""")