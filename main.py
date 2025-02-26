import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import base64
from pathlib import Path

from data.materials_database import WEATHER_CONDITIONS, TRAFFIC_LOADS, SOIL_TYPES
from utils.recommendation_engine import get_recommendations

# Page configuration
st.set_page_config(
    page_title="Road Construction Material Recommender",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header with custom styling and watermark
st.markdown("""
    <div class='title-section'>
        <div class='title-content'>
            <h1 style='font-size: 2.5em; margin-bottom: 1rem;'>🛣️ Road Construction Material Recommender</h1>
            <p style='font-size: 1.2em; color: #999;'>
                Material recommendations for modern road construction projects
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Parameter Input Form
st.markdown("<div class='parameter-form'>", unsafe_allow_html=True)
st.header("Project Parameters")

col1, col2 = st.columns(2)
with col1:
    location = st.text_input("Project Location", "", help="Enter the construction site location")
    traffic_load = st.selectbox(
        "Traffic Load",
        options=TRAFFIC_LOADS,
        help="Expected traffic volume on the road"
    )

with col2:
    weather = st.selectbox(
        "Weather Conditions",
        options=WEATHER_CONDITIONS,
        help="Predominant weather conditions in the area"
    )
    soil_type = st.selectbox(
        "Soil Type",
        options=SOIL_TYPES,
        help="Type of soil at the construction site"
    )

st.markdown("</div>", unsafe_allow_html=True)

# Generate recommendations when form is submitted
if st.button("Generate Recommendations", key="generate_btn"):
    if not location:
        st.error("Please enter a project location")
    else:
        with st.spinner('Analyzing parameters and generating recommendations...'):
            params = {
                'location': location,
                'traffic_load': traffic_load,
                'weather': weather,
                'soil_type': soil_type
            }

            recommendations = get_recommendations(params)

            # Display recommendations
            st.header("Recommended Materials")

            # Top recommendation
            with st.container():
                st.markdown("""
                    <div style='background: rgba(31, 31, 31, 0.7); padding: 2rem; border-radius: 8px; margin-bottom: 2rem;'>
                """, unsafe_allow_html=True)

                st.subheader("Best Match")
                top_recommendation = recommendations[0]

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"### {top_recommendation['material']}")
                    st.markdown(f"**Suitability Score:** {top_recommendation['score']:.1f}%")
                    st.markdown("### Key Advantages")
                    for advantage in top_recommendation['advantages']:
                        st.markdown(f"✓ {advantage}")

                with col2:
                    # Radar chart with material properties
                    properties = top_recommendation['properties']
                    fig = go.Figure()
                    fig.add_trace(go.Scatterpolar(
                        r=list(properties.values()),
                        theta=list(properties.keys()),
                        fill='toself',
                        name=top_recommendation['material'],
                        line_color='#1E88E5'
                    ))
                    fig.update_layout(
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, 10],
                                gridcolor="rgba(255, 255, 255, 0.1)",
                                color="white"
                            ),
                            bgcolor="rgba(0,0,0,0)"
                        ),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font_color="white",
                        showlegend=True,
                        height=600,
                        width=None
                    )
                    st.plotly_chart(fig, use_container_width=True)

                st.markdown("</div>", unsafe_allow_html=True)

            # Comparison table
            st.subheader("Material Comparison")
            comparison_data = []
            for rec in recommendations:
                comparison_data.append({
                    'Material': rec['material'],
                    'Suitability Score': f"{rec['score']:.1f}%",
                    'Durability': rec['properties']['durability'],
                    'Cost Factor': rec['properties']['cost'],
                    'Weather Resistance': rec['properties']['weather_resistance'],
                    'Load Capacity': rec['properties']['load_capacity']
                })

            df = pd.DataFrame(comparison_data)
            st.table(df)

            # Bar chart comparison
            fig = px.bar(
                df,
                x='Material',
                y=['Durability', 'Cost Factor', 'Weather Resistance', 'Load Capacity'],
                title="Material Properties Comparison",
                barmode='group',
                template="plotly_dark",
                height=600
            )
            fig.update_layout(
                xaxis_title="Material",
                yaxis_title="Rating (0-10)",
                legend_title="Properties",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                showlegend=True,
                margin=dict(l=50, r=50, t=50, b=50)
            )
            st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem;'>
    <p style='color: #666;'>Road Construction Material Recommender System</p>
    <p style='color: #666;'>Built with Streamlit • Professional Engineering Tool</p>
</div>
""", unsafe_allow_html=True)