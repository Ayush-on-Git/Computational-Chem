import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from data.materials_database import WEATHER_CONDITIONS, TRAFFIC_LOADS, SOIL_TYPES
from utils.recommendation_engine import get_recommendations

# Page configuration
st.set_page_config(
    page_title="Road Construction Material Recommender",
    page_icon="🛣️",
    layout="wide"
)

# Load custom CSS
with open('styles/custom.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
st.title("Road Construction Material Recommender")
st.markdown("""
This system helps engineers and construction professionals determine 
the most suitable materials for road construction based on various parameters.
""")

# Parameter Input Form
st.header("Project Parameters")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.text_input("Project Location", "")
        traffic_load = st.selectbox("Traffic Load", options=TRAFFIC_LOADS)
        
    with col2:
        weather = st.selectbox("Weather Conditions", options=WEATHER_CONDITIONS)
        soil_type = st.selectbox("Soil Type", options=SOIL_TYPES)

# Generate recommendations when form is submitted
if st.button("Generate Recommendations"):
    if not location:
        st.error("Please enter a project location")
    else:
        # Get recommendations
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
            st.subheader("Best Match")
            top_recommendation = recommendations[0]
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"### {top_recommendation['material']}")
                st.markdown(f"**Suitability Score:** {top_recommendation['score']:.1f}%")
                st.markdown("### Advantages")
                for advantage in top_recommendation['advantages']:
                    st.markdown(f"- {advantage}")
                    
            with col2:
                # Radar chart for properties
                properties = top_recommendation['properties']
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(
                    r=list(properties.values()),
                    theta=list(properties.keys()),
                    fill='toself',
                    name=top_recommendation['material']
                ))
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                    showlegend=True
                )
                st.plotly_chart(fig)
        
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
            barmode='group'
        )
        fig.update_layout(
            xaxis_title="Material",
            yaxis_title="Rating (0-10)",
            legend_title="Properties"
        )
        st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Road Construction Material Recommender System</p>
    <p>Built with Streamlit • Professional Engineering Tool</p>
</div>
""", unsafe_allow_html=True)
