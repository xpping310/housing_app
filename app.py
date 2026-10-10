import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('California Housing Data (1990) by xpp')

df = pd.read_csv('housing.csv')

house_value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)

st.subheader('See more filters in the sidebar:')

location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())

income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High'))

df = df[df.median_house_value >= house_value_filter]

df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

st.map(df)

st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots()
df.median_house_value.plot.hist(ax=ax, bins=30)
st.pyplot(fig)