# Standard Library
import os
import time

# Third Party
import streamlit as st

# Local Imports
from process_resume import process_resume
from agents import (
    analyze_resume,
    chat_with_resume,
)

def render_upload_page():

    st.markdown(
        "<div class='main-title'>📄 Resume Copilot</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>AI Powered Resume Intelligence</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='big-space'></div>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        uploaded_file = st.file_uploader(
            "Upload Resume",
            type=["pdf"],
            label_visibility="collapsed"
        )

        st.markdown(
            """
            <h3>Drop your Resume here</h3>
            <p>Supported format : PDF</p>
            """,
            unsafe_allow_html=True
        )

        if uploaded_file is not None:

            os.makedirs("uploads", exist_ok=True)

            file_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            progress = st.progress(0)
            status = st.empty()

            status.info("Uploading Resume...")
            progress.progress(20)

            time.sleep(0.5)

            status.info("Reading Resume...")
            progress.progress(40)

            time.sleep(0.5)

            status.info("Creating Embeddings...")
            progress.progress(70)

            process_resume(file_path)

            time.sleep(0.5)

            status.success("Resume Processed Successfully ✅")
            progress.progress(100)

            st.session_state.resume_processed = True
            st.session_state.resume_path = file_path

            time.sleep(1)

            st.session_state.page = "job"

            st.rerun()


def render_job_page():

    st.markdown(
        "<div class='main-title'>🎯 Resume Analysis</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Tell us which job you are targeting</div>",
        unsafe_allow_html=True
    )

    st.write("")

    role = st.text_input(
        "Target Role",
        placeholder="Example : AI Engineer"
    )

    st.write("")

    job_description = st.text_area(
        "Job Description",
        placeholder="Paste complete Job Description here...",
        height=250
    )

    st.write("")

    col1, col2, col3 = st.columns([2, 2, 2])

    with col2:

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        )

    if analyze:

        if role.strip() == "" or job_description.strip() == "":

            st.warning(
                "Please enter Target Role and Job Description."
            )

        else:

            with st.spinner("Analyzing Resume..."):

                analysis = analyze_resume(
                    role=role,
                    job_description=job_description
                )

                st.session_state.analysis = analysis
                st.session_state.role = role
                st.session_state.job_description = job_description

                time.sleep(1)

                st.session_state.page = "dashboard"

                st.rerun()


def render_dashboard():
    
    st.markdown("""
    <style>

    .dashboard-card{

        background:black;

        border-radius:20px;

        padding:30px;

        box-shadow:0px 10px 30px rgba(0,0,0,.08);

        margin-bottom:25px;

    }

    .section-title{

        font-size:26px;

        font-weight:700;

        margin-bottom:20px;

    }

    </style>
    """, unsafe_allow_html=True)

    top1, top2 = st.columns([6,2])

    with top1:

        st.markdown(
            "# 📄 Resume Dashboard"
        )

    with top2:

        if st.button(
            "💬 Talk to Resume",
            use_container_width=True
        ):

            st.session_state.page = "chat"

            st.rerun()

    st.write("")

    # -----------------------------
    # Analysis
    # -----------------------------


    analysis = st.session_state.analysis

    if not analysis:
        st.error("Resume analysis not found.")
        st.stop()
        
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
    <div style="background:#1e293b;
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid #334155;">

    <h4 style="color:#94a3b8;">ATS Score</h4>

    <p style="font-size:60px;
    font-weight:700;
    color:#38bdf8;
    margin:0;">
    {analysis['ats_score']}
    </p>

    </div>
    """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            f"""
    <div style="background:#1e293b;
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid #334155;">

    <h4 style="color:#94a3b8;">Resume Match</h4>

    <p style="font-size:60px;
    font-weight:700;
    color:#22c55e;
    margin:0;">
    {analysis['resume_match']}%
    </p>

    </div>
    """,
            unsafe_allow_html=True,
        )

    # --------------------------------------------------
    # Professional Summary
    # --------------------------------------------------

    st.markdown("## 👤 Professional Summary")

    st.info(
        analysis["professional_summary"]
    )

    st.write("")

    # --------------------------------------------------
    # Technical Skills
    # --------------------------------------------------

    st.markdown("## 🛠 Technical Skills")

    skills = analysis.get("technical_skills", [])

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            with cols[i % 4]:
                st.markdown(
                    f"""
    <div style="
    background:#2563eb;
    padding:10px;
    border-radius:25px;
    text-align:center;
    font-weight:600;
    color:white;
    margin-bottom:10px;
    ">
    {skill}
    </div>
    """,
                    unsafe_allow_html=True
                )

    # --------------------------------------------------
    # Missing Skills & Keywords
    # --------------------------------------------------

    left, right = st.columns(2)

    # Missing Skills
    with left:

        st.markdown("## 🚫 Missing Skills")

        missing_skills = analysis.get("missing_skills", [])

        if missing_skills:

            for skill in missing_skills:
                st.error(skill)

        else:
            st.success("No major missing skills found.")

    # Missing Keywords
    with right:

        st.markdown("## 🔍 Missing Keywords")

        missing_keywords = analysis.get("missing_keywords", [])

        if missing_keywords:

            for keyword in missing_keywords:
                st.warning(keyword)

        else:
            st.success("No missing keywords found.")

    # --------------------------------------------------
    # Strengths && Weaknesses
    # --------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.markdown("## ✅ Strengths")

        for strength in analysis["strengths"]:
            st.success(strength)

    with right:

        st.markdown("## ⚠️ Weaknesses")

        for weakness in analysis["weaknesses"]:
            st.warning(weakness)

    # --------------------------------------------------
    # Suggestions
    # --------------------------------------------------

    st.markdown("## 💡 Suggestions")

    for suggestion in analysis["suggestions"]:
        st.info(suggestion)

    st.write("")

    # --------------------------------------------------
    # Final Verdict
    # --------------------------------------------------

    st.write("")

    st.markdown("""
    <h2 style="margin-bottom:15px;">
    🎯 Overall Verdict
    </h2>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
    <div style="
    background:#172554;
    padding:25px;
    border-radius:18px;
    border-left:8px solid #3b82f6;
    ">

    <h3 style="color:white;margin-top:0;">
    Resume Evaluation
    </h3>

    <p style="
    font-size:18px;
    line-height:1.8;
    color:#dbeafe;
    margin-bottom:0;
    ">
    {analysis["final_verdict"]}
    </p>

    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chat_page():

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    top1, top2 = st.columns([2, 8])

    with top1:

        if st.button(
            "⬅ Dashboard",
            key="back_to_dashboard"
        ):

            st.session_state.page = "dashboard"
            st.rerun()

    with top2:

        st.markdown("# 💬 Talk to Resume")

    st.write("---")

    # Chat History
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    user_question = st.chat_input(
        "Ask anything about your resume..."
    )

    if user_question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = chat_with_resume(
                    user_question
                )

                st.markdown(response)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )