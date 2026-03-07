import re

# Technical skill dictionary
TECH_SKILLS = {
    "python","java","javascript","react","node","flask","django",
    "sql","mysql","postgresql","mongodb","html","css",
    "machine learning","deep learning","nlp",
    "docker","aws","git","github","tensorflow","pandas",
    "numpy","scikit","rest","api"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def extract_skills(text):

    text = clean_text(text)

    found_skills = []

    for skill in TECH_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def generate_skill_templates(df):

    templates = {}

    for category in df["category"].unique():

        resumes = df[df["category"] == category]

        skill_set = set()

        for text in resumes["resume_text"]:
            skills = extract_skills(text)
            skill_set.update(skills)

        templates[category] = list(skill_set)

    return templates