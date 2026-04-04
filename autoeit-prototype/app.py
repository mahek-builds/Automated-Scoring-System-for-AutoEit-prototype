import streamlit as st
import pandas as pd
from datetime import datetime
from src.engine import  run_scoring

# Page Configuration
st.set_page_config(page_title="AutoEIT - Automated Scoring System", layout="wide")

# Custom CSS for UI styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .session-card { background-color: #ffffff; padding: 15px; border-radius: 8px; border: 1px solid #eee; margin-bottom: 10px; }
    .status-pill { background-color: #d4edda; color: #155724; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
tabs = ["Dashboard", "Score Task", "About"]
selected_tab = st.sidebar.radio("Navigation", tabs)

# --- DASHBOARD PAGE ---
if selected_tab == "Dashboard":
    st.title("📊 AutoEIT Dashboard")
    st.caption("Automated Scoring System for Spanish Elicited Imitation Task")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sessions", "3", help="Scoring sessions completed")
    col2.metric("Sentences Scored", "60", help="Total sentences analyzed")
    col3.metric("Avg Agreement", "94.2%", help="With human raters")
    col4.metric("Avg Time Saved", "45 min", help="Per scoring session")

    st.divider()
    
    st.subheader("Recent Scoring Sessions")
    sessions = [
        {"name": "Spanish EIT Dataset - Cohort A", "date": "2026-04-02", "count": "24 sentences", "score": "98/120"},
        {"name": "Spanish EIT Dataset - Cohort B", "date": "2026-04-01", "count": "24 sentences", "score": "87/120"},
        {"name": "Practice Session - Test Data", "date": "2026-03-30", "count": "12 sentences", "score": "56/60"},
    ]

    for s in sessions:
        with st.container():
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.markdown(f"**{s['name']}**")
            c2.text(s['date'])
            c3.markdown(f"<span class='status-pill'>completed</span>", unsafe_allow_html=True)
            c4.markdown(f"**{s['score']}** Total EIT Score")
            st.divider()

# --- SCORE TASK PAGE ---
elif selected_tab == "Score Task":
    st.title("🆕 New Scoring Session")
    st.info("Upload your Spanish EIT transcription file to begin automated scoring")
    
    with st.form("scoring_form"):
        session_name = st.text_input("Session Name *", placeholder="e.g., Spanish EIT Dataset - Cohort A")
        uploaded_file = st.file_uploader("Upload Transcription File (TXT or CSV only)", type=["csv", "txt"])
        # uploaded_file=r"C:\Users\bhati\Automated-Scoring-System-for-AutoEit-prototype\autoeit-prototype\content\test.csv"

        submit = st.form_submit_button("🚀 Start Scoring", use_container_width=True)
        
        if submit and uploaded_file:
            st.success(f"Processing '{session_name}'...")
            uploaded_file.seek(0)
            scored_df =run_scoring(uploaded_file)
            st.dataframe(scored_df.head())
            output_file = "scored_output.csv"
            scored_df.to_csv(output_file, index=False)
            
    st.markdown("### ℹ️ Requirements")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**File Format**")
        st.caption("CSV: use columns 'stimulus' and 'response'.")
        st.caption("TXT: use format 'Stimulus | Response' on each line.")
    with col_b:
        st.write("**Scoring Engine**")
        st.caption("Hybrid approach: Deterministic rule-based + ML fallback.")

# --- ABOUT PAGE ---
elif selected_tab == "About":
    st.title("📖 About AutoEIT")
    st.markdown("""
    **Project Overview** Addressing reproducibility challenges in Second Language Acquisition (SLA) research. 
    AutoEIT is a fully automated, rubric-faithful scoring engine developed during **GSoC 2026**.
    """)
    
    st.divider()
    
    st.subheader("Technical Architecture")
   
    col_tech, col_team = st.columns(2)
    with col_tech:
        st.write("**Technology Stack**")
        st.code("Python 3.11+, FastAPI, spaCy/NLTK, PyTorch, React, PostgreSQL")
    
    with col_team:
        st.write("**Project Info**")
        st.json({
            "Organization": "HumaniAl / CERN-HSF",
            "Project Size": "Medium (175 Hours)",
            "Difficulty": "Medium"
        })