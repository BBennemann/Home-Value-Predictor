# Home Value Predictor

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.2-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

## About The Project

This project is a machine learning application designed to predict housing sale prices based on a set of features. It includes a data processing and model training pipeline, as well as an interactive web interface for users to get instant price predictions.

This application was built with:
* **Python**
* **Pandas** for data manipulation
* **Scikit-learn** for model creation and data preprocessing
* **Streamlit** for the interactive web UI

This project was developed as a personal study in machine learning and data science, originating from the "House Prices - Advanced Regression Techniques" challenge on Kaggle.

## Project Structure

The repository is organized as follows:

```
.
├── DesafioKaggle/         # Contains the original notebook with the solution for the Kaggle challenge.
├── data/                  # Stores the datasets used for training and testing.
├── models/                # Saved machine learning models after training.
├── ModelGenerator.py      # Script to train and save the prediction model.
├── app.py                 # Script to run the interactive Streamlit web application.
└── requirements.txt       # A list of all necessary Python packages.
```

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have the following installed on your system:
* Python 3.9 or higher
* pip

### Installation

1.  Clone the repository to your local machine.
    ```bash
    git clone https://github.com/BBennemann/Home-Value-Predictor.git
    ```
2.  Navigate to the project directory.
    ```bash
    cd Home-Value-Predictor
    ```
3.  It is highly recommended to create and activate a virtual environment.
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

## Usage Instructions

The project has two main functionalities: training the model and running the web application.

1.  **Train the Prediction Model**

    To train the model with the dataset located in the `/database` folder, run the following command. The trained model will be saved in the `/models` directory.
    ```bash
    python ModelGenerator.py
    ```

2.  **Run the Web Application**

    After the model is trained, you can start the interactive web interface with Streamlit.
    ```bash
    streamlit run app.py
    ```
    Open your browser and go to `http://localhost:8501` to use the application.

## Contributors

* **Bernardo Thomas Bennemann** - *Project Owner* - [BBennemann](https://github.com/BBennemann)
