# ==========================================
# Dummy specifications for regression models
# ==========================================

# Gender dummy definitions
GENDER_DUMMIES_FEMALE_REF = {
    "source_column": "Gender",
    "drop": "Female",
    "prefix": "gender"
}

GENDER_DUMMIES_MALE_REF = {
    "source_column": "Gender",
    "drop": "Male",
    "prefix": "gender"
}

# Privacy dummy definitions
PRIVACY_DUMMIES_NO_REF = {
    "source_column": "Concerns AI",
    "drop": "No",
    "prefix": "privacy"
}

PRIVACY_DUMMIES_NEVER_REF = {
    "source_column": "Concerns AI",
    "drop": "Never thought about it",
    "prefix": "privacy"
}

# ==========================================
# Core regression variables
# ==========================================

BASE_PREDICTORS = [
    "Age",
    "CRT_points",
    "Internet_Understanding_Score",
    "Help of AI",
    "Reliability AI"
]

# Gender dummy variable names (expected columns after dummy creation)
GENDER_VARS_FEMALE_REF = [
    "gender_Männlich",
    "gender_Keine Angabe"
]

GENDER_VARS_MALE_REF = [
    "gender_Weiblich",
    "gender_Keine Angabe"
]

# Privacy dummy variable names
PRIVACY_VARS_NO_REF = [
    "privacy_Ja",
    "privacy_Ich habe darüber noch nie nachgedacht."
]

PRIVACY_VARS_NEVER_REF = [
    "privacy_Ja",
    "privacy_Nein"
]

