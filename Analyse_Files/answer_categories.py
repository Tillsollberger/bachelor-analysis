# Answercategories.py

#defining order for all questions

# Answer order for: Use AI school and education
Use_AI_school_and_freetime_order = [
    "Täglich",
    "Mehrmals pro Woche",
    "Etwa 1 Mal pro Woche",
    "Seltener",
    "Nie"
]

# Answer order for: Frequency of use education
Frequency_of_use_education_order = [
    "Nie",
    "Selten",
    "Manchmal",
    "Oft",
    "Sehr oft"
]

# Answer order for: Frequency of use everyday life
Frequency_of_use_everyday_life_order = [
    "Nie",
    "Selten",
    "Manchmal",
    "Oft",
    "Sehr oft"
]

# Answer order for: Usefullness AI
usefulness_order = [
    "Sehr nützlich",
    "Ziemlich nützlich",
    "Teils/teils",
    "Wenig nützlich",
    "Überhaupt nicht nützlich"
]

# Answer order for: Deal with AI
deal_order = [
    "Sehr gut",
    "Eher gut",
    "Weder gut noch schlecht",
    "Eher schlecht",
    "Gar nicht"
]

# Answer order for: Understanding AI
understanding_order = [
    "Sehr gut",
    "Eher gut",
    "Weder gut noch schlecht",
    "Eher wenig",
    "Gar nicht"
]

# Answer order for: Internet terms 
Internet_terms_order = [
    "Kein Verständnis",
    "Schlechtes Verständnis",
    "Mittelmässiges Verständnis",
    "Gutes Verständnis",
    "Völliges Verständnis"
]

# Answer order for: Internet terms Score
Internet_terms_order_2 = [
    "Sehr schlechtes Verständnis",
    "Schlechtes Verständnis",
    "Mittelmässiges Verständnis",
    "Gutes Verständnis",
    "Sehr gutes Verständnis"
]

# Answer order for: Reliability AI
reliability_order = [
    "Sehr verlässlich",
    "Eher verlässlich",
    "Teils/teils",
    "Wenig verlässlich",
    "Gar nicht verlässlich",
    "Unsicher / Ich habe keine Meinung"
]

# Answer order for: Allowance to use AI
allowance_order = [
    "Ja, für beides",
    "Nur für Hausaufgaben",
    "Nur in der Schule",
    "Nur wenn die Lehrperson es ausdrücklich erlaubt",
    "Nur wenn meine Eltern es erlauben",
    "Nein, weder für die Schule noch für die Hausaufgaben"
]

# Answer order for: Concerns AI
concerns_order = [
    "Ja",
    "Nein",
    "Ich habe darüber noch nie nachgedacht."
]

# Answer order for: Teachers preparing lessons
teachers_preparing_lessons_order = [
    "Stört mich sehr",
    "Stört mich ein wenig",
    "Neutral / Mir egal",
    "Finde ich gut",
    "Finde ich sehr gut"
]

# Answer order for: Teachers giving grades
teachers_giving_grades_order = [
    "Stört mich sehr",
    "Stört mich ein wenig",
    "Neutral / Mir egal",
    "Finde ich gut",
    "Finde ich sehr gut"
]

# Answer order for: Mates using AI
Mates_using_AI_order = [
    "Nie",
    "Selten",
    "Manchmal",
    "Oft",
    "Immer"
]

# Answer order for: Frequency of use AI_school
Frequency_of_use_AI_school_order = [
    "Nie",
    "Selten",
    "Manchmal",
    "Häufig",
    "Immer"
]

# Answer order for: Help of AI
helpfulness_order = [
    "Sehr gut",
    "Eher gut",
    "Neutral",
    "Eher schlecht",
    "Sehr schlecht"
]

hours_per_week_order = [
    "0-1 Stunde pro Woche", 
    "2-5 Stunden pro Woche",
    "Mehr als 5 Stunden pro Woche"
]

true_false_score = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"
]

CRT_order = [
    "0",
    "1",
    "2",
    "3"
]

Age_order = [
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19"
]

# matching order to column names
question_orders = {
    "Usefullness AI": usefulness_order,
    "Deal with AI": deal_order,
    "Understanding AI": understanding_order,
    "Internet terms_Spyware": Internet_terms_order,
    "Internet terms_Cache": Internet_terms_order,
    "Internet terms_Advanced Search": Internet_terms_order,
    "Internet terms_PDF": Internet_terms_order,
    "Internet terms_Phishing": Internet_terms_order,
    "Internet terms_Wiki": Internet_terms_order,
    "Reliability AI": reliability_order,
    "Allowance to use AI": allowance_order,
    "Concerns AI": concerns_order,
    "Help of AI": helpfulness_order,
    "Use AI school and freetime": Use_AI_school_and_freetime_order,
    "Frequency of use education": Frequency_of_use_education_order,
    "Frequency of use everyday life": Frequency_of_use_everyday_life_order,
    "Teachers preparing lessons": teachers_preparing_lessons_order,
    "Teachers giving grades": teachers_giving_grades_order,
    "Mates using AI": Mates_using_AI_order,
    "Frequency use of AI_school": Frequency_of_use_AI_school_order,
    "Hours per week for school": hours_per_week_order,
    "Age": Age_order,
    "CRT_points": CRT_order,
    "Internet_Understanding_Score": Internet_terms_order_2,
    "Internet Understanding (Grouped)": Internet_terms_order_2
}


LABEL_MAPS = {
    # =====================
    # Frequencies of use
    # =====================
    "Use AI school and freetime": {
        "Täglich": "Daily",
        "Mehrmals pro Woche": "Several times a week",
        "Etwa 1 Mal pro Woche": "About once a week",
        "Seltener": "Less often",
        "Nie": "Never",
    },
    "Frequency of use education": {
        "Nie": "Never",
        "Selten": "Rarely",
        "Manchmal": "Sometimes",
        "Oft": "Often",
        "Sehr oft": "Very often",
    },
    "Frequency of use everyday life": {
        "Nie": "Never",
        "Selten": "Rarely",
        "Manchmal": "Sometimes",
        "Oft": "Often",
        "Sehr oft": "Very often",
    },
    "Frequency of use AI_school": {
        "Nie": "Never",
        "Selten": "Rarely",
        "Manchmal": "Sometimes",
        "Häufig": "Often",
        "Immer": "Always",
    },

    # =====================
    # Perceived usefulness / skills
    # =====================
    "Usefulness AI": {
        "Sehr nützlich": "Very useful",
        "Ziemlich nützlich": "Quite useful",
        "Teils/teils": "Neutral",
        "Wenig nützlich": "Not very useful",
        "Überhaupt nicht nützlich": "Not useful at all",
    },
    "Deal with AI": {
        "Sehr gut": "Very good",
        "Eher gut": "Rather good",
        "Weder gut noch schlecht": "Neither good nor bad",
        "Eher schlecht": "Rather bad",
        "Gar nicht": "Not at all",
    },
    "Understanding AI": {
        "Sehr gut": "Very good",
        "Eher gut": "Rather good",
        "Weder gut noch schlecht": "Neither good nor bad",
        "Eher wenig": "Rather little",
        "Gar nicht": "Not at all",
    },
    "Help of AI": {
        "Sehr gut": "Very good",
        "Eher gut": "Rather good",
        "Neutral": "Neutral",
        "Eher schlecht": "Rather bad",
        "Sehr schlecht": "Very bad",
    },

    # =====================
    # Internet terms
    # =====================
    "Internet terms": {
        "Kein Verständnis": "No understanding",
        "Schlechtes Verständnis": "Poor understanding",
        "Mittelmässiges Verständnis": "Moderate understanding",
        "Gutes Verständnis": "Good understanding",
        "Völliges Verständnis": "Complete understanding",
    },
    "Internet terms (Score)": {
        "Sehr schlechtes Verständnis": "Very poor understanding",
        "Schlechtes Verständnis": "Poor understanding",
        "Mittelmässiges Verständnis": "Moderate understanding",
        "Gutes Verständnis": "Good understanding",
        "Sehr gutes Verständnis": "Very good understanding",
    },

    # =====================
    # Reliability
    # =====================
    "Reliability AI": {
        "Sehr verlässlich": "Very reliable",
        "Eher verlässlich": "Rather reliable",
        "Teils/teils": "Neutral",
        "Wenig verlässlich": "Not very reliable",
        "Gar nicht verlässlich": "Not reliable at all",
        "Unsicher / Ich habe keine Meinung": "Unsure / No opinion",
    },

    # =====================
    # Allowance to use AI
    # =====================
    "Allowance to use AI": {
        "Ja, für beides": "Yes, for both",
        "Nur für Hausaufgaben": "Only for homework",
        "Nur in der Schule": "Only at school",
        "Nur wenn die Lehrperson es ausdrücklich erlaubt": "Only if the teacher explicitly allows it",
        "Nur wenn meine Eltern es erlauben": "Only if my parents allow it",
        "Nein, weder für die Schule noch für die Hausaufgaben": "No, neither for school nor homework",
    },

    # =====================
    # Concerns AI
    # =====================
    "Concerns AI": {
        "Ja": "Yes",
        "Nein": "No",
        "Ich habe darüber noch nie nachgedacht.": "I have never thought about it",
    },

    # =====================
    # Teachers
    # =====================
    "Teachers preparing lessons": {
        "Stört mich sehr": "Bothers me a lot",
        "Stört mich ein wenig": "Bothers me a little",
        "Neutral / Mir egal": "Neutral / I don't care",
        "Finde ich gut": "I think it's good",
        "Finde ich sehr gut": "I think it's very good",
    },
    "Teachers giving grades": {
        "Stört mich sehr": "Bothers me a lot",
        "Stört mich ein wenig": "Bothers me a little",
        "Neutral / Mir egal": "Neutral / I don't care",
        "Finde ich gut": "I think it's good",
        "Finde ich sehr gut": "I think it's very good",
    },

    # =====================
    # Mates
    # =====================
    "Mates using AI": {
        "Nie": "Never",
        "Selten": "Rarely",
        "Manchmal": "Sometimes",
        "Oft": "Often",
        "Immer": "Always",
    },

    # =====================
    # Hours per week
    # =====================
    "Hours per week for school": {
        "0-1 Stunde pro Woche": "0–1 hour per week",
        "2-5 Stunden pro Woche": "2–5 hours per week",
        "Mehr als 5 Stunden pro Woche": "More than 5 hours per week",
    },

    # =====================
    # Scores
    # =====================
    "True_False_Score": {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
    },
    "CRT_points": {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
    },
}

