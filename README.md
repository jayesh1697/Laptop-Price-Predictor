# Laptop Price Predictor

This project is a Machine Learning-based application that predicts the price of laptops based on various features such as brand, type, CPU frequency, RAM, GPU, screen resolution, and storage options.

The goal of this project is to provide an accurate estimate of laptop prices using data collected from Kaggle and a Random Forest Regressor model, which achieved an **R² score of 88%**.

## Table of Contents
- [Key Features](#key-features)
- [Methodology](#methodology)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [How to Run the Project](#how-to-run-the-project)
- [Future Scope](#future-scope)

## Key Features
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

## Methodology
The project utilizes a dataset from Kaggle containing information on laptops and their respective prices. Various machine learning models were tested, and the **Random Forest Regressor** was chosen for deployment as it produced the best results, achieving an **88% R² score**.

**Other models tested:**
- Linear Regression
- Decision Trees
- Gradient Boosting

The Random Forest model was selected due to its superior performance in handling non-linear relationships and interactions between features.

## Results
The final model is able to predict laptop prices with an accuracy of **88%**, meaning it can explain 88% of the variance in laptop prices based on the input features.

## Technologies Used
- **Python** (with libraries like scikit-learn, pandas, numpy)
- **Machine Learning Models:** Random Forest Regressor, Decision Trees, etc.
- **Streamlit:** For building an interactive web application.
- **Pickle:** For saving the trained model.

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/laptop-price-predictor.git
cd laptop-price-predictor
