from utils import load_vector_store, generate
from prompts import (
    ANALYSIS_PROMPT,
    SUMMARY_PROMPT,
    SUGGESTION_PROMPT,
    CHAT_PROMPT,
)


def get_resume_context(query: str, k: int = 4):
    """
    Retrieve the most relevant resume chunks from FAISS.
    """

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(
        query=query,
        k=k
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context


def analyze_resume(job_description: str, role: str):
    """
    Analyze resume against Job Description.
    """

    search_query = f"""
    Target Role:
    {role}

    Job Description:
    {job_description}
    """

    context = get_resume_context(search_query)

    human_prompt = f"""
Resume Context:

{context}

Target Role:
{role}

Job Description:

{job_description}
"""

    return generate(
        ANALYSIS_PROMPT,
        human_prompt
    )


def generate_summary():
    """
    Generate professional resume summary.
    """

    context = get_resume_context(
        "Provide a professional summary of this resume. Include key skills, experience, and education." \
        "Keep it concise and recruiter-friendly. Dont give more than 200 words." \
        "Do not add information that is not present in the resume." 
    )

    return generate(
        SUMMARY_PROMPT,
        context
    )

def generate_summary(analysis: str):
    """
    Generate a professional summary based on the resume analysis.
    """

    return generate(
        SUMMARY_PROMPT,
        analysis
    )



def generate_suggestions():
    """
    Generate resume improvement suggestions.
    """

    context = get_resume_context(
        "Suggest improvements for this resume."
    )

    return generate(
        SUGGESTION_PROMPT,
        context
    )

def generate_suggestions(analysis: str):
    """
    Generate resume improvement suggestions.
    """

    return generate(
        SUGGESTION_PROMPT,
        analysis
    )


def chat_with_resume(user_question: str):
    """
    Answer user questions about the resume.
    """

    context = get_resume_context(user_question)

    human_prompt = f"""
Resume Context:

{context}

User Question:
{user_question}
"""

    return generate(
        CHAT_PROMPT,
        human_prompt
    )