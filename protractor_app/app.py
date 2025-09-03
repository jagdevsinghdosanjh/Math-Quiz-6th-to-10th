import streamlit as st
import streamlit.components.v1 as components
from plotly import graph_objects as go

st.set_page_config(page_title="Circular Protractor Viewer", layout="centered")
st.title("🎯 Circular Protractor Viewer")

# Angle inputs
angle1 = st.slider("Start Angle", 0, 360, 40)
angle2 = st.slider("End Angle", 0, 360, 70)

# SVG Visualization
st.subheader("🖼️ SVG Version")

# Simple SVG code for demonstration (replace with your own SVG logic as needed)
svg_code = f"""
<svg width="400" height="400" viewBox="0 0 400 400">
  <circle cx="200" cy="200" r="180" stroke="gray" stroke-width="4" fill="none"/>
  <line x1="200" y1="200" x2="{200 + 180 * __import__('math').cos(__import__('math').radians(angle1))}" y2="{200 - 180 * __import__('math').sin(__import__('math').radians(angle1))}" stroke="blue" stroke-width="4"/>
  <line x1="200" y1="200" x2="{200 + 180 * __import__('math').cos(__import__('math').radians(angle2))}" y2="{200 - 180 * __import__('math').sin(__import__('math').radians(angle2))}" stroke="blue" stroke-width="4"/>
</svg>
"""

components.html(svg_code, height=420)

# Plotly Visualization
st.subheader("📊 Plotly Visualization")

fig = go.Figure()

# Outer circle
fig.add_trace(go.Scatterpolar(
    r=[1]*361,
    theta=list(range(361)),
    mode='lines',
    line=dict(color='lightgray'),
    showlegend=False
))

# Angle lines
fig.add_trace(go.Scatterpolar(
    r=[0, 1],
    theta=[angle1, angle1],
    mode='lines',
    line=dict(color='blue', width=2),
    name=f"{angle1}°"
))
fig.add_trace(go.Scatterpolar(
    r=[0, 1],
    theta=[angle2, angle2],
    mode='lines',
    line=dict(color='blue', width=2),
    name=f"{angle2}°"
))

# Arc between angles
arc_range = list(range(angle1, angle2 + 1)) if angle1 < angle2 else list(range(angle1, 360)) + list(range(0, angle2 + 1))
fig.add_trace(go.Scatterpolar(
    r=[0.9]*len(arc_range),
    theta=arc_range,
    mode='lines',
    line=dict(color='pink', width=4),
    name="Angle Arc"
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=False)),
    showlegend=False,
    margin=dict(t=20, b=20, l=20, r=20),
    height=420
)

st.plotly_chart(fig, use_container_width=True)

# import streamlit as st
# from utils.angle_math import compute_arc # noqa
# import streamlit as st # noqa
# from components.svg_renderer import render_svg
# from plotly import graph_objects as go # noqa

# st.title("Circular Protractor Viewer")

# angle1 = st.slider("Start Angle", 0, 360, 40)
# angle2 = st.slider("End Angle", 0, 360, 70)

# st.subheader("SVG Version")
# svg_code = render_svg(angle1, angle2)
# st.components.v1.html(svg_code, height=420)


# # st.title("Circular Protractor Viewer")

# # angle1 = st.slider("Start Angle", 0, 360, 40)
# # angle2 = st.slider("End Angle", 0, 360, 70)

# st.subheader("Plotly Visualization")
# # (Insert Plotly polar chart logic here)

# st.subheader("SVG Version")
# svg_code = render_svg(angle1, angle2)
# st.components.v1.html(svg_code, height=400)
