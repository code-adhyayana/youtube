import streamlit as st
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("student_data.csv")
df["Full_ID"] = df["ID"].astype('str') + "-" + df["Name"]

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("Student Performance Dashboard")

selected_student = st.sidebar.selectbox("Select Student", df["Full_ID"].tolist())
st.sidebar.markdown("---")

student_details = df[df["Full_ID"] == selected_student]
new_student_details = student_details.drop(columns=["Full_ID"])
st.subheader(f"Details for {selected_student}")
st.dataframe(new_student_details)

st.subheader("Performance Overview")

student_scores = student_details.drop(columns=["ID", "Full_ID"]).melt(id_vars=["Name"], var_name="Subject", value_name="Marks")

average_scores = df.drop(columns=["ID", "Name", "Full_ID"]).mean().reset_index()
average_scores.columns = ["Subject", "Average Marks"]

max_scores = df.drop(columns=["ID", "Name", "Full_ID"]).max().reset_index()
max_scores.columns = ["Subject", "Max Marks"]

min_scores = df.drop(columns=["ID", "Name", "Full_ID"]).min().reset_index()
min_scores.columns = ["Subject", "Min Marks"]

fig = go.Figure()

fig.add_trace(go.Bar(
    x=student_scores["Subject"],
    y=student_scores["Marks"],
    name=selected_student,
    marker_color='lightskyblue'
))

fig.add_trace(go.Scatter(
    x=average_scores["Subject"],
    y=average_scores["Average Marks"],
    mode='markers',
    name='Average',
    marker=dict(color='black', size=10, symbol='circle')
))

fig.add_trace(go.Scatter(
    x=max_scores["Subject"],
    y=max_scores["Max Marks"],
    mode='markers',
    name='Highest',
    marker=dict(color='green', size=10, symbol='circle')
))

fig.add_trace(go.Scatter(
    x=min_scores["Subject"],
    y=min_scores["Min Marks"],
    mode='markers',
    name='Lowest',
    marker=dict(color='red', size=10, symbol='circle')
))

fig.update_layout(
    title=f"Performance Comparison: {selected_student} vs Class Stats",
    xaxis_title="Subject",
    yaxis_title="Marks",
    barmode='group'
)

st.plotly_chart(fig)
