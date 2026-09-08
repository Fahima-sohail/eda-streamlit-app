# Exploratory Data Analysis Interface (Streamlit)

An interactive Streamlit app for exploratory data analysis (EDA) — upload a CSV, inspect its metadata, and visualize any column dynamically.

**Live app:** ADD_YOUR_STREAMLIT_APP_LINK_HERE

## Features
- CSV file upload with format validation
- Dataset preview (first 5 rows)
- Metadata panel: shape, column data types, missing values (count + %), statistical summary
- Dynamic attribute selector in the sidebar
- Automatic numerical vs. categorical detection
  - Numerical → histogram
  - Categorical → bar chart with frequency and percentage labels

## Tested With
[Titanic-Dataset.csv](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

## Project Structure
```
├── task1.py           # Main Streamlit application
├── requirements.txt   # Python dependencies
└── README.md
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run task1.py
```
Then open the local URL Streamlit prints (usually http://localhost:8501) and upload a CSV from the sidebar.

## Deployment
Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud), connected to this GitHub repo (branch: `main`, main file: `task1.py`). The app auto-redeploys on every push to `main`.

## Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib