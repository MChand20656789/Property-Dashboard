import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

import sys
from pathlib import Path

# Add project root (property-dashboard/) to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.crud import count_properties, avg_price_by_state

st.set_page_config(page_title="Real Estate Dashboard", layout="wide")
st.title("Real Estate Analytics Dashboard")

st.metric("Total Properties (Sample)", count_properties())

engine = create_engine("sqlite:///data/property.db", connect_args={"check_same_thread": False})
df = pd.read_sql("SELECT * FROM properties LIMIT 1000", engine)

st.subheader("Sample Data")
st.dataframe(df.head(20))

st.subheader("Top States by Avg Price")
avg_df = pd.DataFrame(avg_price_by_state(), columns=["State", "Avg_Price"])
st.bar_chart(avg_df.set_index("State"))


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

st.subheader("Simple Price Prediction Demo")

df_ml = df[['price', 'bed', 'bath', 'house_size', 'acre_lot']].dropna()
if len(df_ml) > 50:
    X = df_ml[['bed','bath','house_size','acre_lot']].astype(float)
    y = df_ml['price'].astype(float)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(X_train, y_train)
    score = model.score(X_test, y_test)
    st.write(f"Model R²: {score:.2f}")

    bed = st.number_input("Beds", 1, 8, 3)
    bath = st.number_input("Baths", 1, 8, 2)
    size = st.number_input("House Size (sqft)", 200, 8000, 1500)
    acre = st.number_input("Acre Lot", 0.0, 5.0, 0.2, step=0.1)

    # Wrap user input in a DataFrame with matching feature names
    X_new = pd.DataFrame([[bed, bath, size, acre]], columns=["bed", "bath", "house_size", "acre_lot"])
    pred = model.predict(X_new)[0]
    st.metric("Predicted Price", f"${pred:,.0f}")

st.sidebar.header("Filters")
states = sorted(df['state'].dropna().unique().tolist())
state = st.sidebar.selectbox("Filter by State", ["All"] + states)
if state != "All":
    df = df[df['state'] == state]

st.subheader(f"Price Distribution ({state})")
fig, ax = plt.subplots()
df['price'].dropna().astype(float).hist(bins=30, ax=ax, color='skyblue')
st.pyplot(fig)
    

