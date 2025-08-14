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
    "18"
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
