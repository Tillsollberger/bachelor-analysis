# answer_categories.py
# Definition of category orders for survey variables
# Used for descriptive statistics, plots, and cross-tabulations

from __future__ import annotations

# --------------------------------------------------
# Category orders for individual questions
# --------------------------------------------------

USE_AI_SCHOOL_FREETIME_ORDER = [
    "Täglich",
    "Mehrmals pro Woche",
    "Etwa 1 Mal pro Woche",
    "Seltener",
    "Nie",
]

FREQUENCY_OF_USE_ORDER = [
    "Nie",
    "Selten",
    "Manchmal",
    "Oft",
    "Sehr oft",
]

USEFULNESS_AI_ORDER = [
    "Sehr nützlich",
    "Ziemlich nützlich",
    "Teils/teils",
    "Wenig nützlich",
    "Überhaupt nicht nützlich",
]

DEAL_WITH_AI_ORDER = [
    "Sehr gut",
    "Eher gut",
    "Weder gut noch schlecht",
    "Eher schlecht",
    "Gar nicht",
]

UNDERSTANDING_AI_ORDER = [
    "Sehr gut",
    "Eher gut",
    "Weder gut noch schlecht",
    "Eher wenig",
    "Gar nicht",
]

INTERNET_TERMS_ORDER = [
    "Kein Verständnis",
    "Schlechtes Verständnis",
    "Mittelmässiges Verständnis",
    "Gutes Verständnis",
    "Völliges Verständnis",
]

RELIABILITY_AI_ORDER = [
    "Sehr verlässlich",
    "Eher verlässlich",
    "Teils/teils",
    "Wenig verlässlich",
    "Gar nicht verlässlich",
    "Unsicher / Ich habe keine Meinung",
]

ALLOWANCE_TO_USE_AI_ORDER = [
    "Ja, für beides",
    "Nur für Hausaufgaben",
    "Nur in der Schule",
    "Nur wenn die Lehrperson es ausdrücklich erlaubt",
    "Nur wenn meine Eltern es erlauben",
    "Nein, weder für die Schule noch für die Hausaufgaben",
]

CONCERNS_AI_ORDER = [
    "Ja",
    "Nein",
    "Ich habe darüber noch nie nachgedacht.",
]

TEACHERS_AI_ORDER = [
    "Stört mich sehr",
    "Stört mich ein wenig",
    "Neutral / Mir egal",
    "Finde ich gut",
    "Finde ich sehr gut",
]

MATES_USING_AI_ORDER = [
    "Nie",
    "Selten",
    "Manchmal",
    "Oft",
    "Immer",
]

FREQUENCY_USE_AI_SCHOOL_ORDER = [
    "Nie",
    "Selten",
    "Manchmal",
    "Häufig",
    "Immer",
]

HELP_OF_AI_ORDER = [
    "Sehr gut",
    "Eher gut",
    "Neutral",
    "Eher schlecht",
    "Sehr schlecht",
]

HOURS_PER_WEEK_ORDER = [
    "0-1 Stunde pro Woche",
    "2-5 Stunden pro Woche",
    "Mehr als 5 Stunden pro Woche",
]

TRUE_FALSE_SCORE_ORDER = ["0", "1", "2", "3", "4", "5", "6"]
CRT_ORDER = ["0", "1", "2", "3"]
AGE_ORDER = [str(x) for x in range(11, 20)]


# --------------------------------------------------
# Canonical column name mapping
# --------------------------------------------------

COLUMN_ALIASES = {
    "Usefullness AI": "Usefulness AI",
    "UsefulnessAI": "Usefulness AI",
}


# --------------------------------------------------
# Mapping of columns to category orders
# -------------------------------------------------- 

question_orders = {
    "Use AI school and freetime": USE_AI_SCHOOL_FREETIME_ORDER,
    "Frequency of use education": FREQUENCY_OF_USE_ORDER,
    "Frequency of use everyday life": FREQUENCY_OF_USE_ORDER,
    "Usefulness AI": USEFULNESS_AI_ORDER,
    "Deal with AI": DEAL_WITH_AI_ORDER,
    "Understanding AI": UNDERSTANDING_AI_ORDER,
    "Reliability AI": RELIABILITY_AI_ORDER,
    "Concerns AI": CONCERNS_AI_ORDER,
    "Allowance to use AI": ALLOWANCE_TO_USE_AI_ORDER,
    "Teachers preparing lessons": TEACHERS_AI_ORDER,
    "Teachers giving grades": TEACHERS_AI_ORDER,
    "Mates using AI": MATES_USING_AI_ORDER,
    "Frequency use of AI_school": FREQUENCY_USE_AI_SCHOOL_ORDER,
    "Help of AI": HELP_OF_AI_ORDER,
    "Hours per week for school": HOURS_PER_WEEK_ORDER,
    "Age": AGE_ORDER,
    "CRT_points": CRT_ORDER,
    "True_False_Score": TRUE_FALSE_SCORE_ORDER,
    "Internet terms_Spyware": INTERNET_TERMS_ORDER,
    "Internet terms_Cache": INTERNET_TERMS_ORDER,
    "Internet terms_Advanced Search": INTERNET_TERMS_ORDER,
    "Internet terms_PDF": INTERNET_TERMS_ORDER,
    "Internet terms_Phishing": INTERNET_TERMS_ORDER,
    "Internet terms_Wiki": INTERNET_TERMS_ORDER,
    "Internet Understanding (Grouped)": INTERNET_TERMS_ORDER,
}


