import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Housing App",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Housing App")

# Resolve CSV path reliably in Streamlit
base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "housing.csv"

if not csv_path.exists():
    st.error("⚠️ Error: housing.csv file not found. Please make sure the CSV file is in the same folder as app.py.")
    st.stop()

# Load data
try:
    df = pd.read_csv(csv_path)
except Exception as e:
    st.error(f"⚠️ Failed to load housing.csv: {e}")
    st.stop()

# Sidebar navigation
page = st.sidebar.radio(
    "Select a page",
    ["Home", "Data Analysis"],
    index=0
)

# Home page
if page == "Home":
    st.header("Welcome to the Housing App!")
    st.write("This application helps you explore and analyze housing data with ease.")

    st.divider()

    st.subheader("About This App")
    st.info("""
    This is a single-entry Streamlit application designed to provide insights into housing data.

    **Features:**
    - Explore housing data interactively
    - Filter by house value, location type, and income level
    - Visualize data on maps and histograms

    Use the sidebar to navigate between pages.
    """)

# Data Analysis page
elif page == "Data Analysis":
    st.header("California Housing Data (1990)")

    # Main filter
    st.subheader("Filters")
    house_value_filter = st.slider(
        'Minimal Median House Value',
        int(df['median_house_value'].min()),
        int(df['median_house_value'].max()),
        200000
    )

    # Sidebar filters
    location_filter = st.sidebar.multiselect(
        'Choose the location type',
        df['ocean_proximity'].unique(),
        df['ocean_proximity'].unique()
    )

    income_filter = st.sidebar.radio(
        'Choose income level',
        ('Low', 'Medium', 'High')
    )

    # Apply filters
    filtered_df = df[df['median_house_value'] >= house_value_filter]
    filtered_df = filtered_df[filtered_df['ocean_proximity'].isin(location_filter)]

    if income_filter == 'Low':
        filtered_df = filtered_df[filtered_df['median_income'] <= 2.5]
    elif income_filter == 'Medium':
        filtered_df = filtered_df[(filtered_df['median_income'] > 2.5) & (filtered_df['median_income'] < 4.5)]
    elif income_filter == 'High':
        filtered_df = filtered_df[filtered_df['median_income'] >= 4.5]

    # Display data count
    st.metric("Records Shown", len(filtered_df))

    # Map
    st.subheader("Location Map")
    st.map(filtered_df)

    # Histogram
    st.subheader('Histogram of Median House Value')
    fig, ax = plt.subplots(figsize=(10, 6))
    filtered_df['median_house_value'].plot.hist(ax=ax, bins=30, edgecolor='black')
    ax.set_xlabel('Median House Value')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
