import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Load data from SQLite
db_path = "data/airtravel.db"
engine = create_engine(f"sqlite:///{db_path}")
df = pd.read_sql("SELECT * FROM flights", engine)

# Sidebar - year selection
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))

# Filter data
filtered_df = df[df["Year"] == int(year)]

# Title
st.title("Air Travel Dashboard (1958–1960)")
st.write(f"Monthly passenger numbers for {year}")

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(filtered_df["Month"], filtered_df["Passengers"], color="skyblue")
ax.set_ylabel("Passengers")
ax.set_xlabel("Month")
ax.set_title(f"Air Passengers in {year}")
st.pyplot(fig)

# Summary
st.markdown("### Total passengers by year")
summary = df.groupby("Year")["Passengers"].sum().reset_index()
st.dataframe(summary)
