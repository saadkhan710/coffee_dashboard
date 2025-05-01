# ☕ Coffee Shop Sales Analytics Dashboard

## Overview
A comprehensive analytics dashboard for Borcelle Coffee Shop, providing real-time insights into sales performance, customer behavior, and business operations. Built with Streamlit and Python, this interactive dashboard helps owners make data-driven decisions.

## ✨ Features
- 📊 **Sales Analytics**: Track revenue, transactions, and trends
- 🏷️ **Category Performance**: Analyze product category sales
- 📍 **Location Insights**: Compare performance across store locations
- ⏱️ **Peak Hours Analysis**: Identify busiest times for staffing
- 🏆 **About Section**: Showcase cafe history, team, and values


## 🛠️ Technologies Used
- Python 3.9+
- Streamlit (Web framework)
- Pandas (Data manipulation)
- Plotly (Interactive visualizations)
- Prophet (Time series forecasting)
- Pillow (Image processing)

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https: https://github.com/saadkhan710/coffee_dashboard.git
cd coffee_dashboard

# 2. Set up virtual environment
python -m venv borcelle_env

# Windows activation:
.\borcelle_env\Scripts\activate

# macOS/Linux activation:
source borcelle_env/bin/activate
```

## 🔧 Installation Issues

```bash

# If Prophet fails to install:
conda install -c conda-forge prophet

# Windows users - virtual env activation:
Set-ExecutionPolicy Unrestricted -Scope Proces

```
## ⚠️ Troubleshooting

```bash

# 3. Install dependencies
pip install -r requirements.txt  # If you have the file
# OR
pip install streamlit pandas plotly prophet pillow

```

## Add required files to project root:
- cleaned_coffee_shop_data.csv (your sales data)
- assets/jason-leung-poI7DelFiVA-unsplash.jpg
- assets/oguz-yagiz-kara-MZf0mI14RI0-unsplash.jpg
- assets/vicky-hladynets-C8Ta0gwPbQg-unsplash.jpg
- assets/logo.png (brand logo)
- assets/Owner.jpeg (founder photo)

## Launch the dashboard
```bash
streamlit run dashboard.py

```
## Project Structure
```bash
borcelle-dashboard/
├── dashboard.py             # Main application
├── requirements.txt         # Dependencies
├── cleaned_coffee_shop_data.csv  # Sales data
└── assets/                  # Additional images (create this folder)
    ├── jason-leung-poI7DelFiVA-unsplash.jpg
    ├── oguz-yagiz-kara-MZf0mI14RI0-unsplash.jpg
    ├──vicky-hladynets-C8Ta0gwPbQg-unsplash.jpg
    ├── logo.png                 # Brand logo
    ├── Owner.jpeg               # Founder photo

```

## 🌐 Live Demo

Access the dashboard at: https://coffee-shop-analytics-dashboard.streamlit.app/
