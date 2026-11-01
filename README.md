# Urban Traffic Intelligence

An interactive traffic analytics and machine learning dashboard built using Python, Streamlit, Pandas and Plotly.

## Project Overview

Urban Traffic Intelligence analyses historical vehicle-count data across four junctions to identify traffic patterns, compare junction activity and evaluate machine learning prediction models.

## Key Features

- Interactive traffic analytics dashboard
- Junction-wise traffic comparison
- Hourly and weekday traffic analysis
- Historical traffic trend visualisation
- Machine learning model performance evaluation
- Actual vs predicted traffic analysis
- Interactive filters and KPI metrics

## Technology Stack

- Python
- Streamlit
- Pandas and NumPy
- Plotly
- Scikit-learn
- Machine Learning

## Dataset

The project uses a historical traffic dataset containing 48,120 records across four junctions, covering November 2015 to June 2017.

The dataset contains timestamps, junction identifiers and vehicle counts.

**Note:** Vehicle counts are used as a traffic-volume indicator. They do not directly measure congestion, vehicle speed, travel time or road capacity.

## Machine Learning

The project evaluates:
- Linear Regression
- Random Forest
- HistGradientBoosting
- Mean Baseline

Models are compared using MAE, RMSE and R².

## Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/urban-traffic-intelligence.git
cd urban-traffic-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Author

**Yaseen Akthar Maniyar**

B.Tech — Artificial Intelligence & Robotics

Dayananda Sagar University, Bengaluru

## Disclaimer

This project is intended for educational and analytical purposes using historical traffic data. It is not a live traffic monitoring system.
