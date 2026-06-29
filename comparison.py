def compare_items(resume_items, required_items):
    insight = {
        "already_covered": [],
        "missing": [],
    }

    for item in resume_items:
        if item in required_items:
            insight["already_covered"].append(item)

    for item in required_items:
        if item not in resume_items:
            insight["missing"].append(item)

    return insight


def compare_resume_job(resume_analysis, job_analysis):
    details = {
        "technical_skills": compare_items(resume_analysis["technical_skills"], job_analysis["technical_skills"]),
        "programming_languages": compare_items(resume_analysis["programming_languages"],
                                               job_analysis["programming_languages"]),
        "tools": compare_items(resume_analysis["tools"], job_analysis["tools"])
    }

    return details
