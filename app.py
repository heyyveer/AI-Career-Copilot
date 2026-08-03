# import os
# import streamlit as st

# from process_resume import process_resume
# from agents import (
#     analyze_resume,
#     generate_summary,
#     generate_suggestions,
#     chat_with_resume,
# )

# # -----------------------------
# # Page Config
# # -----------------------------
# st.set_page_config(
#     page_title="Resume Copilot",
#     page_icon="📄",
#     layout="wide",
# )

# st.title("📄 Resume Copilot")
# st.write("AI Powered Resume Analyzer & Resume Chat Assistant")

# # -----------------------------
# # Session State
# # -----------------------------
# if "resume_processed" not in st.session_state:
#     st.session_state.resume_processed = False

# if "analysis" not in st.session_state:
#     st.session_state.analysis = ""

# # -----------------------------
# # Upload Resume
# # -----------------------------
# st.header("📤 Upload Resume")

# uploaded_file = st.file_uploader(
#     "Upload Resume (PDF)",
#     type=["pdf"]
# )

# if uploaded_file:

#     os.makedirs("uploads", exist_ok=True)

#     file_path = os.path.join(
#         "uploads",
#         uploaded_file.name
#     )

#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     if st.button("Process Resume"):

#         with st.spinner("Processing Resume..."):

#             try:
#                 process_resume(file_path)
#                 st.session_state.resume_processed = True
#                 st.success("Resume Processed Successfully!")
#             except Exception as e:
#                 st.error(f"Error processing resume: {str(e)}")
#                 st.session_state.resume_processed = False

# # -----------------------------
# # Resume Analysis
# # -----------------------------
# if st.session_state.resume_processed:

#     st.divider()

#     st.header("🎯 Resume Analysis")

#     role = st.text_input(
#         "Target Role",
#         placeholder="AI Engineer"
#     )

#     job_description = st.text_area(
#         "Job Description",
#         height=250,
#         placeholder="Paste Job Description Here..."
#     )

#     if st.button("Analyze Resume"):

#         if not role or not job_description:
#             st.warning("Please provide both Target Role and Job Description.")
#         else:
#             with st.spinner("Analyzing Resume..."):

#                 try:
#                     analysis = analyze_resume(
#                         role=role,
#                         job_description=job_description
#                     )

#                     summary = generate_summary()

#                     suggestions = generate_suggestions()

#                     st.session_state.analysis = analysis
#                     st.session_state.summary = summary
#                     st.session_state.suggestions = suggestions
#                 except Exception as e:
#                     st.error(f"Error analyzing resume: {str(e)}")

#     # Display Results
#     if st.session_state.analysis:
#         st.subheader("📊 Analysis Results")
#         st.markdown(st.session_state.analysis)

#         st.subheader("📝 Professional Summary")
#         st.markdown(st.session_state.summary)

#         st.subheader("💡 Improvement Suggestions")
#         st.markdown(st.session_state.suggestions)

# # -----------------------------
# # Chat with Resume
# # -----------------------------
# if st.session_state.resume_processed:

#     st.divider()

#     st.header("💬 Chat with Resume")

#     # Initialize chat history
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     # Display chat history
#     for message in st.session_state.chat_history:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Chat input
#     if user_question := st.chat_input("Ask a question about the resume..."):

#         # Add user message to chat history
#         st.session_state.chat_history.append({
#             "role": "user",
#             "content": user_question
#         })

#         # Display user message
#         with st.chat_message("user"):
#             st.markdown(user_question)

#         # Generate response
#         with st.chat_message("assistant"):
#             with st.spinner("Thinking..."):
#                 response = chat_with_resume(user_question)
#                 st.markdown(response)

#         # Add assistant response to chat history
#         st.session_state.chat_history.append({
#             "role": "assistant",
#             "content": response
#         })




import os
import time
import streamlit as st

from process_resume import process_resume

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

header{
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

if "resume_processed" not in st.session_state:
    st.session_state.resume_processed = False

if "resume_path" not in st.session_state:
    st.session_state.resume_path = None

# ---------------------------------------------------
# Upload Screen
# ---------------------------------------------------

if st.session_state.page == "upload":

    st.markdown(
        "<div class='main-title'>📄 Resume Copilot</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>AI Powered Resume Intelligence</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='big-space'></div>", unsafe_allow_html=True)

    left, center, right = st.columns([1,2,1])

    with center:

        # st.markdown("<div class='upload-card'>", unsafe_allow_html=True)

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

        st.markdown("</div>", unsafe_allow_html=True)

        # -----------------------------
        # Auto Process Resume
        # -----------------------------

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

# ---------------------------------------------------
# Job Description Screen
# ---------------------------------------------------

from agents import (
    analyze_resume,
    chat_with_resume,
    generate_summary,
    generate_suggestions,
)

if "analysis" not in st.session_state:
    st.session_state.analysis = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "suggestions" not in st.session_state:
    st.session_state.suggestions = ""


if st.session_state.page == "job":

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

    col1, col2, col3 = st.columns([2,2,2])

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

                summary = generate_summary(
                    analysis
                )

                suggestions = generate_suggestions(
                    analysis
                )

                st.session_state.analysis = analysis
                st.session_state.summary = summary
                st.session_state.suggestions = suggestions

                st.session_state.role = role
                st.session_state.job_description = job_description

                time.sleep(1)

                st.session_state.page = "dashboard"

                st.rerun()



# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

if st.session_state.page == "dashboard":

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
    # Summary Card
    # -----------------------------

    st.markdown(
        """
        <div class='dashboard-card'>
        <div class='section-title'>
        👤 Professional Summary
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        st.session_state.summary
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------
    # Analysis
    # -----------------------------

    st.markdown(
        """
        <div class='dashboard-card'>
        <div class='section-title'>
        📊 Resume Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        st.session_state.analysis
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------
    # Suggestions
    # -----------------------------

    st.markdown(
        """
        <div class='dashboard-card'>
        <div class='section-title'>
        💡 Improvement Suggestions
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        st.session_state.suggestions
    )

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------------------------------------------
# Chat Page
# ---------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.session_state.page == "chat":

    top1, top2 = st.columns([2,8])

    with top1:

        if st.button("⬅ Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

    with top2:

        st.markdown("# 💬 Talk to Resume")

    st.write("---")

    # Display Chat History
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    user_question = st.chat_input(
        "Ask anything about your resume..."
    )

    if user_question:

        # User Message
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        with st.chat_message("user"):
            st.markdown(user_question)

        # AI Response
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