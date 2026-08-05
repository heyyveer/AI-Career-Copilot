
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

from ui import (
    render_sidebar,
    render_dashboard,
    render_chat_page,
    render_job_page,
    render_upload_page,
)

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Resume Copilot",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# Hide Streamlit Default UI
# ---------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
max-width:1100px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

html,
body,
[class*="css"]{
font-family:Inter,sans-serif;
}

.main-title{
text-align:center;
font-size:52px;
font-weight:800;
margin-top:40px;
margin-bottom:10px;
}

.sub-title{
text-align:center;
font-size:20px;
color:#8b8b8b;
margin-bottom:60px;
}

.upload-card{

border:2px dashed #5B8DEF;

border-radius:25px;

padding:70px;

text-align:center;

transition:.3s;

background:black;

box-shadow:0px 10px 30px rgba(0,0,0,.06);

}

.upload-card:hover{

transform:translateY(-4px);

box-shadow:0px 20px 40px rgba(0,0,0,.12);

}

.big-space{

margin-top:80px;

}

.stApp{

background: linear-gradient(
135deg,
#0f172a,
#1e293b,
#111827
);

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "upload"

if "feature" not in st.session_state:
    st.session_state.feature = "home"

if "resume_processed" not in st.session_state:
    st.session_state.resume_processed = False

if "resume_path" not in st.session_state:
    st.session_state.resume_path = None

# ---------------------------------------------------
# Upload Screen
# ---------------------------------------------------

if st.session_state.page == "upload":
    render_upload_page()

# ---------------------------------------------------
# Job Description Screen
# ---------------------------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = ""


if st.session_state.page == "job":
    render_job_page()

# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

if st.session_state.page == "dashboard":
    render_sidebar()
    render_dashboard()

# ---------------------------------------------------
# Chat Page
# ---------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.session_state.page == "chat":
    render_sidebar()
    render_chat_page()