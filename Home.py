import streamlit as st

st.set_page_config(
    page_title="Housing App Home",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Housing App")

st.write("""
Welcome to the Housing App! This application helps you explore and analyze housing data with ease.

Use the navigation menu on the left to explore different features and pages.
""")

col1, col2, col3 = st.columns(3)

with col2:
    if st.button("📊 Go to App", use_container_width=True):
        st.switch_page("pages/app.py")

st.divider()

st.subheader("About This App")
st.info("""
This is a multipage Streamlit application designed to provide insights into housing data.
Navigate through the different pages using the sidebar menu to access various features.
""")
