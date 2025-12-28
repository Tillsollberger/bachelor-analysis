# lists.py

from __future__ import annotations


demographic_columns = [
    "Gender",
    "Age",
    "Education Level",
    "Preferred Subjects",
    "Least preferred Subjects",
    "Educational Level parent_1",
    "Educational Level parent_2",
    "CRT_points",
]

single_choice_questions = [
    "Gender",
    "Age",
    "Education Level",
    "Educational Level parent_1",
    "Educational Level parent_2",
    "CRT_points",
    "Use AI school and freetime",
    "Frequency of use education",
    "Frequency of use everyday life",
    "Usefulness AI",
    "Deal with AI",
    "Understanding AI",
    "Internet terms_Spyware",
    "Internet terms_Cache",
    "Internet terms_Advanced Search",
    "Internet terms_PDF",
    "Internet terms_Phishing",
    "Internet terms_Wiki",
    "True_False_Score",
    "Reliability AI",
    "Concerns AI",
    "Teachers preparing lessons",
    "Teachers giving grades",
    "Mates using AI",
    "Allowance to use AI",
    "Frequency use of AI_school",
    "Help of AI",
    "Internet Understanding (Grouped)",
]

multiple_choice_questions = [
    "Reasons to use AI",
    "Purposes to use AI",
    "Most used subjects",
    "Used AI",
    "Use of AI in freetime",
    "Preferred Subjects",
    "Least preferred Subjects",
]

true_false_questions = [
    "True/False_1",
    "True/False_2",
    "True/False_3",
    "True/False_4",
    "True/False_5",
    "True/False_6",
]

true_false_solutions = {
    "True/False_1": "Falsch",
    "True/False_2": "Falsch",
    "True/False_3": "Falsch",
    "True/False_4": "Falsch",
    "True/False_5": "Wahr",
    "True/False_6": "Falsch",
}

Internet_terms_mapping = {
    "Völliges Verständnis": 5,
    "Gutes Verständnis": 4,
    "Mittelmässiges Verständnis": 3,
    "Schlechtes Verständnis": 2,
    "Kein Verständnis": 1,
}

comparison_pairs_by_demo = {
    "Gender": [
        "Use AI school and freetime",
        "Usefulness AI",
        "Most used subjects",
    ],
    "Age": [
        "Use AI school and freetime",
        "Deal with AI",
        "Understanding AI",
        "Concerns AI",
        "Internet Understanding (Grouped)",
    ],
    "Hours per week for school": [
        "Frequency of use education",
    ],
}

comparison_pairs_by_AI_questions = {
    "Use AI school and freetime": [
        "Usefulness AI",
        "Concerns AI",
        "Reliability AI",
        "Mates using AI",
        "Deal with AI",
        "Understanding AI",
    ],
    "Used AI": [
        "Reliability AI",
    ],
    "Reliability AI": [
        "Teachers preparing lessons",
        "Teachers giving grades",
    ],
    "Frequency use of AI_school": [
        "Help of AI",
        "Reasons to use AI (Count)",
        "Purposes to use AI (Count)",
    ],
}

likert_questions = [
    "Use AI school and freetime",
    "Frequency of use education",
    "Frequency of use everyday life",
    "Usefulness AI",
    "Deal with AI",
    "Understanding AI",
    "Reliability AI",
    "Help of AI",
    "Mates using AI",
    "Teachers preparing lessons",
    "Teachers giving grades",
    "Internet Understanding (Grouped)",
    "True_False_Score",
]

LIKERT_VALUE_MAPS = {
    "Use AI school and freetime": {
        "Täglich": 5,
        "Mehrmals pro Woche": 4,
        "Etwa 1 Mal pro Woche": 3,
        "Seltener": 2,
        "Nie": 1,
    },
    "Frequency of use education": {
        "Sehr oft": 5,
        "Oft": 4,
        "Manchmal": 3,
        "Selten": 2,
        "Nie": 1,
    },
    "Frequency of use everyday life": {
        "Sehr oft": 5,
        "Oft": 4,
        "Manchmal": 3,
        "Selten": 2,
        "Nie": 1,
    },
    "Usefulness AI": {
        "Sehr nützlich": 5,
        "Ziemlich nützlich": 4,
        "Teils/teils": 3,
        "Wenig nützlich": 2,
        "Überhaupt nicht nützlich": 1,
    },
    "Deal with AI": {
        "Sehr gut": 5,
        "Eher gut": 4,
        "Weder gut noch schlecht": 3,
        "Eher schlecht": 2,
        "Gar nicht": 1,
    },
    "Understanding AI": {
        "Sehr gut": 5,
        "Eher gut": 4,
        "Weder gut noch schlecht": 3,
        "Eher wenig": 2,
        "Gar nicht": 1,
    },
    "Reliability AI": {
        "Sehr verlässlich": 5,
        "Eher verlässlich": 4,
        "Teils/teils": 3,
        "Wenig verlässlich": 2,
        "Gar nicht verlässlich": 1,
        "Unsicher / Ich habe keine Meinung": 3,
    },
    "Help of AI": {
        "Sehr gut": 5,
        "Eher gut": 4,
        "Neutral": 3,
        "Eher schlecht": 2,
        "Sehr schlecht": 1,
    },
    "Mates using AI": {
        "Immer": 5,
        "Oft": 4,
        "Manchmal": 3,
        "Selten": 2,
        "Nie": 1,
    },
    "Teachers preparing lessons": {
        "Finde ich sehr gut": 5,
        "Finde ich gut": 4,
        "Neutral / Mir egal": 3,
        "Stört mich ein wenig": 2,
        "Stört mich sehr": 1,
    },
    "Teachers giving grades": {
        "Finde ich sehr gut": 5,
        "Finde ich gut": 4,
        "Neutral / Mir egal": 3,
        "Stört mich ein wenig": 2,
        "Stört mich sehr": 1,
    },
    "Internet Understanding (Grouped)": {
        "Völliges Verständnis": 5,
        "Gutes Verständnis": 4,
        "Mittelmässiges Verständnis": 3,
        "Schlechtes Verständnis": 2,
        "Kein Verständnis": 1,
    },
    "True_False_Score": {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
    },
}

cross_tab_titles_and_colors = {
    ("Gender", "Use AI school and freetime"): [
        "AI usage (school + free time) by gender",
        "#74af8f",
        "#4a90e2",
        "#e74c3c",
    ],
    ("Gender", "Usefulness AI"): ["Perceived usefulness of AI by gender"],
    ("Gender", "Most used subjects"): ["Most used school subjects for AI by gender"],
    ("Gender", "Help of AI"): ["Perceived helpfulness of AI by gender"],
    ("Age", "Use AI school and freetime"): ["AI usage (school + free time) by age"],
    ("Age", "Deal with AI"): ["Confidence dealing with AI by age"],
    ("Age", "Understanding AI"): ["Self-rated understanding of AI by age"],
    ("Age", "Concerns AI"): ["Concerns about AI by age"],
    ("Age", "Help of AI"): ["Perceived helpfulness of AI by age"],
    ("Preferred Subjects", "Most used subjects"): [
        "Most used school subjects for AI by preferred subjects"
    ],
    ("Least preferred Subjects", "Most used subjects"): [
        "Most used school subjects for AI by least preferred subjects"
    ],
    ("Hours per week for school", "Frequency of use education"): [
        "AI usage frequency in education by hours per week spent for school in free time"
    ],
}

nominal_posthoc_pairs_demo = [
    ("Usefulness AI", "Gender"),
    ("Help of AI", "Gender"),
    ("Concerns AI", "Age"),
]

ordinal_posthoc_pairs_demo = [
    ("Use AI school and freetime", "Age"),
    ("True_False_Score", "Age"),
    ("Internet Understanding (Grouped)", "Age"),
]
