import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Data Visualizer")

# Placeholder for dataset

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df)

if uploaded_file:
    st.sidebar.header("Visualization Options")
    
    # Let user pick columns for visualization
    x_axis = st.sidebar.selectbox("Choose X-axis", df.columns)
    y_axis = st.sidebar.selectbox("Choose Y-axis", df.columns)
    chart_type = st.sidebar.selectbox("Choose Chart Type", ["Scatter", "Line", "Bar"])
    
    # Create the chart based on user selection
    if chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis, title="Scatter Plot")
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis, title="Line Chart")
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis, title="Bar Chart")

    st.plotly_chart(fig)
