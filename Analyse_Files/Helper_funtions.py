import pandas as pd
import random
from scipy.stats import chi2_contingency, ttest_ind, f_oneway
from lists import true_false_solutions, Internet_terms_mapping
from answer_categories import question_orders

#function to analyze the distribution of subjects
def analyze_subject_distribution(df, column, title=None):

    if title:
        print(f"\n{title}")
    else:
        print(f"\nSubject distribution for: {column}")

    # Drop empty or NaN responses
    clean_column = df[column].dropna().astype(str).str.strip()
    clean_column = clean_column[clean_column != ""]

    # Number of valid responses (for percentage calculation)
    valid_respondents = clean_column.shape[0]

    # Split comma-separated values, explode and strip whitespace
    exploded = clean_column.str.split(",").explode().str.strip()

    # Count and percentage
    counts = exploded.value_counts()
    percentages = (counts / valid_respondents * 100).round(1)

    result = pd.DataFrame({
        "Mentions": counts,
        "Percentage of respondents": percentages
    })

    print(result)

#function to analyze distribution of demographic questions
def analyze_distribution(df, column, title=None):

    # Drop empty values
    clean_series = df[column].dropna().astype(str).str.strip()
    clean_series = clean_series[clean_series != ""]

    if title:
        print(f"\n{title}")
    else:
        print(f"\nDistribution for: {column}")

    value_counts = clean_series.value_counts()
    percent_counts = clean_series.value_counts(normalize=True) * 100

    # Apply predefined order if available
    if column in question_orders:
        predefined_order = [val for val in question_orders[column] if val in value_counts.index]
        remaining_values = [val for val in value_counts.index if val not in predefined_order]
        final_order = predefined_order + remaining_values

        value_counts = value_counts.reindex(final_order, fill_value=0)
        percent_counts = percent_counts.reindex(final_order, fill_value=0)

    result = pd.DataFrame({
        "Count": value_counts,
        "Percentage": percent_counts.round(1)
    })

    print(result)

# function to test significance of single choice questions
def test_significance_single_choice(df, question_col, demo_col):
    data = df[[question_col, demo_col]].dropna()

    # if both columns are numeric → t-Test / ANOVA
    if pd.api.types.is_numeric_dtype(data[question_col]) and pd.api.types.is_numeric_dtype(data[demo_col]):
        groups = [data[data[demo_col] == val][question_col] for val in data[demo_col].unique()]
        if len(groups) == 2:
            _, p = ttest_ind(*groups)
        else:
            _, p = f_oneway(*groups)
        return p
    else:
        # Always Chi² for categorial data
        contingency = pd.crosstab(data[demo_col], data[question_col])
        chi2, p, *_ = chi2_contingency(contingency)
        return p

# function test the significance of multiple choice questions
def test_significance_multiple_choice(exploded_df, question_col, demo_col):
    
    results = []

    options = exploded_df[question_col].dropna().unique()
    for option in options:
        # new column: either option was chosen or not
        exploded_df[option] = exploded_df[question_col] == option

        contingency = pd.crosstab(exploded_df[demo_col], exploded_df[option])
        try:
            chi2, p, _, _ = chi2_contingency(contingency)
            significance = "✅ significant" if p < 0.05 else "❌ not significant"
            results.append({
                "Option": option,
                "p_value": round(p, 4),
                "Significance": significance
            })
        except Exception as e:
            results.append({
                "Option": option,
                "Error": str(e)
            })
    return results

# funtion to calculate the amount of correct answered True/false questions
def calculate_true_false_score(df):
    
    df["True_False_Score"] = df[list(true_false_solutions.keys())].apply(
        lambda row: sum(row[q] == true_false_solutions[q] for q in true_false_solutions), axis=1
    )
    
    return df

# funtion to calculate the score of internet understanding
def calculate_Internet_terms_understanding_score(df):
    internet_cols = [col for col in df.columns if col.startswith("Internet terms_")]

    df_mapped = df[internet_cols].replace(Internet_terms_mapping)

    df["Internet_Understanding_Score"] = df_mapped.sum(axis=1, min_count=1)

    return df

def group_internet_understanding(df):
    bins = [0, 10, 15, 20, 25, 30]
    labels = [
        "Kein Verständnis",
        "Schlechtes Verständnis",
        "Mittelmässiges Verständnis",
        "Gutes Verständnis",
        "Völliges Verständnis"
    ]
    df["Internet Understanding (Grouped)"] = pd.cut(
        df["Internet_Understanding_Score"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )
    return df

#function to take 3 random subjects if more where given
def clean_up_subjects(df, columnname, max_subjects = 3):
    #set a seed to have always the same output
    random.seed(1)
    
    def clean_up_answer(answer):
        if pd.isna(answer):
            return answer
        subjects = [subject.strip() for subject in answer.split(",")]
        if len(subjects) > max_subjects:
            return ", ".join(random.sample(subjects, max_subjects))
        else:
            return ", ".join(subjects)
        
    df[columnname] = df[columnname].apply(clean_up_answer)
    return df

def analyze_distribution_changed(df, column, title=None, return_df=False):
    clean_series = df[column].dropna().astype(str).str.strip()
    clean_series = clean_series[clean_series != ""]

    value_counts = clean_series.value_counts()
    percent_counts = clean_series.value_counts(normalize=True) * 100

    if column in question_orders:
        predefined_order = [val for val in question_orders[column] if val in value_counts.index]
        remaining_values = [val for val in value_counts.index if val not in predefined_order]
        final_order = predefined_order + remaining_values
        value_counts = value_counts.reindex(final_order, fill_value=0)
        percent_counts = percent_counts.reindex(final_order, fill_value=0)

    result = pd.DataFrame({
        "Count": value_counts,
        "Percentage": percent_counts.round(1)
    })

    if return_df:
        return result
    else:
        print(f"\n{title or column}")
        print(result)

def analyze_subject_distribution_changed(df, column, title=None, return_df=False):
    if title:
        print(f"\n{title}")
    else:
        print(f"\nSubject distribution for: {column}")

    clean_column = df[column].dropna().astype(str).str.strip()
    clean_column = clean_column[clean_column != ""]
    valid_respondents = clean_column.shape[0]

    exploded = clean_column.str.split(",").explode().str.strip()
    counts = exploded.value_counts()
    percentages = (counts / valid_respondents * 100).round(1)

    result = pd.DataFrame({
        "Mentions": counts,
        "Percentage of respondents": percentages
    })

    if return_df:
        return result
    else:
        print(result)
