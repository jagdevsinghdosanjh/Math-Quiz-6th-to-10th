# app.py
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Polar Pole Plot", layout="centered")

st.title("🌍 Polar Visualization – North & South Poles")

# Define polar sectors
fig = go.Figure()

# North Pole sector (0° to 90°)
fig.add_trace(go.Scatterpolar(
    r=[1, 1],
    theta=[0, 90],
    mode='lines',
    line=dict(color='blue', width=4),
    fill='toself',
    name='North Pole'
))

# South Pole sector (180° to 270°)
fig.add_trace(go.Scatterpolar(
    r=[1, 1],
    theta=[180, 270],
    mode='lines',
    line=dict(color='red', width=4),
    fill='toself',
    name='South Pole'
))

# Layout settings
fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=False),
        angularaxis=dict(
            tickmode='array',
            tickvals=[0, 90, 180, 270],
            ticktext=['0°', '90°', '180°', '270°']
        )
    ),
    showlegend=True,
    title="Plotly Polar Representation of Poles"
)

st.plotly_chart(fig, use_container_width=True)
