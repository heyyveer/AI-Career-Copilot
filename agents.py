import json

from prompts import (
    ANALYSIS_PROMPT,
    CHAT_PROMPT,
)

from utils import (
    generate,
    load_vector_store,
)


DEFAULT_TOP_K = 4


def parse_json_response(response: str) -> dict:
    """
    Safely parse JSON returned by the LLM.
    Removes markdown code fences if present.
    """

    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    try:
        return json.loads(response)

    except json.JSONDecodeError:

        return {
            "ats_score": 0,
            "resume_match": 0,
            "professional_summary": "Unable to generate summary.",
            "strengths": [],
            "weaknesses": [],
            "missing_skills": [],
            "missing_keywords": [],
            "experience_feedback": "",
            "project_feedback": "",
            "education_feedback": "",
            "formatting_feedback": "",
            "suggestions": [],
            "recommended_certifications": [],
            "recommended_projects": [],
            "final_verdict": "Analysis failed. Please try again."
        }


def get_resume_context(query: str, k: int = DEFAULT_TOP_K):
    """
    Retrieve relevant resume chunks from FAISS.
    """

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(
        query=query,
        k=k
    )

    context = ""

    for doc in docs:

        page = doc.metadata.get("page", "Unknown")

        context += f"""
Page: {page}

Content:
{doc.page_content}

----------------------------------------
"""

    return context


def analyze_resume(role: str, job_description: str):
    """
    Analyze resume against a Job Description.
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

    response = generate(
        ANALYSIS_PROMPT,
        human_prompt
    )
    print(response)
    return parse_json_response(response)


def chat_with_resume(user_question: str):
    """
    Chat with resume using RAG.
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