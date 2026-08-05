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

from ui import (
    render_chat_page,
    render_upload_page,
    render_job_page,
    render_dashboard,
)

if st.session_state.page == "upload":
    render_upload_page()

# ---------------------------------------------------
# Job Description Screen
# ---------------------------------------------------

from agents import (
    chat_with_resume,
)

if "analysis" not in st.session_state:
    st.session_state.analysis = ""


if st.session_state.page == "job":
    render_job_page()



# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

if st.session_state.page == "dashboard":

    render_dashboard()


# ---------------------------------------------------
# Chat Page
# ---------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.session_state.page == "chat":
    render_chat_page()