import streamlit as st
from components.svg_renderer import render_svg
from utils.angle_math import compute_arc

st.title("Circular Protractor Viewer")

angle1 = st.slider("Start Angle", 0, 360, 40)
angle2 = st.slider("End Angle", 0, 360, 70)

st.subheader("Plotly Visualization")
from plotly import graph_objects as go
# (Insert Plotly polar chart logic here)

st.subheader("SVG Version")
svg_code = render_svg(angle1, angle2)
st.components.v1.html(svg_code, height=400)
