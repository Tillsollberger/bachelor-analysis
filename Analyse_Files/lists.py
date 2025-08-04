# file to store all lists


# all demographic columns
demographic_columns = [
    "Gender",
    "Age",
    "Education Level",
    "Preferred Subjects",
    "Least preferred Subjects",
    "Educational Level parent_1",
    "Educational Level parent_2",
    "CRT_points"
]

# all single choice columns, either demographic or questions about AI
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
    "Usefullness AI",
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
    "Internet Understanding (Grouped)"
]

# all multiple choice columns, either demographic or questions about AI
multiple_choice_questions = [
    "Reasons to use AI",
    "Purposes to use AI",
    "Most used subjects",
    "Used AI",
    "Use of AI in freetime",
    "Preferred Subjects",
    "Least preferred Subjects"
]

# all true/false questions
true_false_questions = [
    "True/False_1",
    "True/False_2",
    "True/False_3",
    "True/False_4",
    "True/False_5",
    "True/False_6"
]

#correct answers to the true/false questions
true_false_solutions = {
    "True/False_1": "Falsch",
    "True/False_2": "Falsch",
    "True/False_3": "Falsch",
    "True/False_4": "Falsch",
    "True/False_5": "Wahr",
    "True/False_6": "Falsch"
}

# Dictionary: for every demographic question a list of AI questions to analyze
comparison_pairs_by_demo = {
    "Gender": [
        "Use AI school and freetime",
        "Usefullness AI",
        "Most used subjects",
        "Help of AI"
        
    ],
    "Age": [
        "Use AI school and freetime",
        "Deal with AI",
        "Understanding AI",
        "Concerns AI",
        "Help of AI",
        "True_False_Score",
        "Internet Understanding (Grouped)"
    ],
    "Hours per week for school": [
        "Frequency of use education",
        "Understanding AI"
    ],
}

# Dictionary: for every AI question a list of AI questions to analyze
comparison_pairs_by_AI_questions = {
    "Use AI school and freetime": [
        "Usefullness AI",
        "Concerns AI",
        "Most used subjects",
        "Reliability AI",
        "Mates using AI",
        "Help of AI"
    ],
    "Used AI": [
        "Reliability AI",
        "Concerns AI"
    ],
    "Understanding AI": [
        "Deal with AI",
        "True_False_Score",
        "Internet Understanding (Grouped)"
    ],
    "Internet Understanding (Grouped)": [
        "True_False_Score"
    ],
    "Reliability AI": [
        "Teachers preparing lessons",
        "Teachers giving grades"
    ],
    "Frequency of use AI_school": [
        "Help of AI"
    ]

}

Internet_terms_mapping = {
   "Völliges Verständnis": 5,
    "Gutes Verständnis": 4,
    "Mittelmässiges Verständnis": 3,
    "Schlechtes Verständnis": 2,
    "Kein Verständnis": 1 
}

# all likert scale questions
likert_questions = [
    "Use AI school and freetime",
    "Frequency of use education",
    "Frequency of use everyday life",
    "Usefullness AI",
    "Deal with AI",
    "Understanding AI",
    "Reliability AI",
    "Teachers preparing lessons",
    "Teachers giving grades",
    "Mates using AI",
    "Frequency use of AI_school",
    "Help of AI"
]

# matching numbers to the likert scale questions
likert_mapping = {
    "Sehr gut": 5,
    "Eher gut": 4,
    "Neutral": 3,
    "Eher schlecht": 2,
    "Sehr schlecht": 1,

    "Immer": 5,
    "Häufig": 4,
    "Manchmal": 3,
    "Selten": 2,
    "Nie": 1,

    "Immer": 5,
    "Oft": 4,
    "Neutral": 3,
    "Selten": 2,
    "Nie": 1,

    "Finde ich sehr gut": 5,
    "Finde ich gut": 4,
    "Neutral / Mir egal": 3,
    "Stört mich ein wenig": 2,
    "Stört mich sehr": 1,

    "Sehr verlässlich": 5,
    "Eher verlässlich": 4,
    "Teils/teils": 3,
    "Wenig verlässlich": 2,
    "Gar nicht verlässlich": 1,
    "Unsicher / Ich habe keine Meinung": 3,

    "Völliges Verständnis": 5,
    "Gutes Verständnis": 4,
    "Mittelmässiges Verständnis": 3,
    "Schlechtes Verständnis": 2,
    "Kein Verständnis": 1,

    "Sehr gut": 5,
    "Eher gut": 4,
    "Weder gut noch schlecht": 3,
    "Eher wenig": 2,
    "Gar nicht": 1,

    "Sehr gut": 5,
    "Eher gut": 4,
    "Weder gut noch schlecht": 3,
    "Eher schlecht": 2,
    "Gar nicht": 1,

    "Sehr nützlich": 5,
    "Ziemlich nützlich": 4,
    "Teils/teils": 3,
    "Wenig nützlich": 2,
    "Überhaupt nicht nützlich": 1,

    "Sehr oft": 5,
    "Oft": 4,
    "Manchmal": 3,
    "Selten": 2,
    "Nie": 1,

    "Täglich": 5,
    "Mehrmals pro Woche": 4,
    "Etwa 1 Mal pro Woche": 3,
    "Seltener": 2,
    "Nie": 1,

    "Schlecht": 2

}
