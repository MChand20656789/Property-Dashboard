# Real Estate Analytics Dashboard

An interactive data dashboard built with **Streamlit**, **SQLAlchemy**, and **scikit-learn** using real U.S. property listings from Kaggle.  
Visualize property prices, explore housing trends, and predict home values based on features.

## Features
- Load & visualize 2M+ property listings (sampled for performance)
- Filter by state, view price distributions, and summary metrics
- Predict property prices using a simple linear regression model
- Real-time dashboard powered by Streamlit

## Tech Stack
- Python (pandas, scikit-learn, matplotlib, seaborn)
- Streamlit for interactive UI
- SQLite for data storage
- SQLAlchemy for ORM and database operations

## Project Structure
```
app/           → Database + CRUD operations  
dashboard/     → Streamlit app interface  
scripts/       → Data import and analysis tools  
data/          → Datasets (local only, not tracked in GitHub)
```

 ## Data Source
This project uses the **[USA Real Estate Dataset](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset)** from Kaggle.

After cloning this repository, download the dataset manually:

1. Visit the Kaggle dataset page.  
2. Download the file `realtor-data.csv`.  
3. Place it in the `data/` folder:

   ```
   data/realtor-data.csv
   ```
4. Then run:
   ```bash
   python scripts/import_data.py
   ```
   to create your local database (`data/property.db`).


## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/property-dashboard.git
   cd property-dashboard
   ```
2. Create the environment:
   ```bash
   conda env create -f environment.yml
   conda activate property-dashboard
   ```
3. Run the dashboard:
   ```bash
   streamlit run dashboard/dashboard_app.py
   ```


## Next Steps
- Add model persistence (save/load trained model)
- Add advanced ML models (Random Forest, XGBoost)
- Deploy to Streamlit Cloud
