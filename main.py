import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
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

# Load and encode background image
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header with custom styling and watermark
st.markdown("""
    <div class='title-section'>
        <div class='title-content'>
            <h1 style='font-size: 2.5em; margin-bottom: 1rem;'>🛣️ Road Construction Material Recommender</h1>
            <p style='font-size: 1.2em; color: #999;'>
                Advanced material recommendations for modern road construction projects
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
                    st.markdown(f"**Overall Score:** {top_recommendation['score']:.1f}%")

                    # Detailed scores
                    st.markdown("### Detailed Analysis")
                    scores = top_recommendation['detailed_scores']
                    st.markdown(f"🏗️ Load Capacity: {scores['load_capacity']:.1f}/10")
                    st.markdown(f"💰 Cost Efficiency: {scores['cost_efficiency']:.1f}/10")
                    st.markdown(f"🌱 Environmental Impact: {scores['environmental_impact']:.1f}/10")
                    st.markdown(f"🌡️ Weather Resistance: {scores['weather_resistance']:.1f}/10")

                    # Maintenance predictions
                    st.markdown("### Maintenance Predictions")
                    predictions = top_recommendation['maintenance_predictions']
                    st.markdown(f"🔄 Maintenance Interval: {predictions['interval_years']:.1f} years")
                    st.markdown(f"💵 Annual Maintenance Cost Factor: {predictions['annual_cost_factor']:.2f}")

                with col2:
                    # Radar chart with updated metrics
                    detailed_scores = top_recommendation['detailed_scores']
                    fig = go.Figure()
                    fig.add_trace(go.Scatterpolar(
                        r=[
                            scores['load_capacity'],
                            scores['cost_efficiency'],
                            scores['environmental_impact'],
                            scores['weather_resistance'],
                            top_recommendation['properties']['durability']
                        ],
                        theta=[
                            'Load Capacity',
                            'Cost Efficiency',
                            'Environmental Impact',
                            'Weather Resistance',
                            'Durability'
                        ],
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

            # Comparison table with advanced metrics
            st.subheader("Material Comparison")
            comparison_data = []
            for rec in recommendations:
                comparison_data.append({
                    'Material': rec['material'],
                    'Overall Score': f"{rec['score']:.1f}%",
                    'Load Capacity': rec['detailed_scores']['load_capacity'],
                    'Cost Efficiency': rec['detailed_scores']['cost_efficiency'],
                    'Environmental Impact': rec['detailed_scores']['environmental_impact'],
                    'Weather Resistance': rec['detailed_scores']['weather_resistance'],
                    'Maintenance Interval (Years)': rec['maintenance_predictions']['interval_years']
                })

            df = pd.DataFrame(comparison_data)
            st.table(df)

            # Advanced metrics comparison chart
            fig = px.bar(
                df,
                x='Material',
                y=['Load Capacity', 'Cost Efficiency', 'Environmental Impact', 'Weather Resistance'],
                title="Advanced Material Properties Comparison",
                barmode='group',
                template="plotly_dark",
                height=600
            )
            fig.update_layout(
                xaxis_title="Material",
                yaxis_title="Score (0-10)",
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