from __future__ import annotations

import hashlib
from typing import Optional

import pandas as pd
import numpy as np

from lists import true_false_solutions, Internet_terms_mapping
from answer_categories import question_orders


def _clean_series(series: pd.Series) -> pd.Series:
    s = series.dropna().astype(str).str.strip()
    return s[s != ""]


def analyze_distribution(
    df: pd.DataFrame,
    column: str,
    title: Optional[str] = None,
    return_df: bool = False,
) -> Optional[pd.DataFrame]:
    """
    Frequency table for a single-choice column.
    Applies question_orders if available.
    """
    clean_series = _clean_series(df[column])

    value_counts = clean_series.value_counts(dropna=False)
    percent_counts = (value_counts / value_counts.sum() * 100).round(1)

    if column in question_orders:
        predefined = [v for v in question_orders[column] if v in value_counts.index]
        remaining = [v for v in value_counts.index if v not in predefined]
        order = predefined + remaining
        value_counts = value_counts.reindex(order, fill_value=0)
        percent_counts = percent_counts.reindex(order, fill_value=0)

    result = pd.DataFrame({"Count": value_counts, "Percentage": percent_counts})

    if return_df:
        return result

    print(f"\n{title or f'Distribution for: {column}'}")
    print(result)
    return None


def analyze_subject_distribution(
    df: pd.DataFrame,
    column: str,
    title: Optional[str] = None,
    return_df: bool = False,
) -> Optional[pd.DataFrame]:
    """
    Frequency table for comma-separated multi-choice columns.
    Percentage refers to respondents, not mentions.
    """
    clean_col = _clean_series(df[column])
    valid_respondents = int(clean_col.shape[0])

    exploded = clean_col.str.split(",").explode().str.strip()
    counts = exploded.value_counts()
    percentages = (counts / valid_respondents * 100).round(1)

    result = pd.DataFrame({"Mentions": counts, "Percentage of respondents": percentages})

    if return_df:
        return result

    print(f"\n{title or f'Subject distribution for: {column}'}")
    print(result)
    return None


def calculate_true_false_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds True_False_Score as number of correct answers across true_false_solutions keys.
    """
    cols = list(true_false_solutions.keys())
    df["True_False_Score"] = df[cols].apply(
        lambda row: sum(row[q] == true_false_solutions[q] for q in cols),
        axis=1
    )
    return df


def calculate_internet_terms_understanding_score(df: pd.DataFrame) -> pd.DataFrame:
    # Adds Internet_Understanding_Score by mapping Internet terms_* columns to 1..5 and summing.
    
    internet_cols = [c for c in df.columns if c.startswith("Internet terms_")]
    df_mapped = df[internet_cols].replace(Internet_terms_mapping)
    df["Internet_Understanding_Score"] = df_mapped.sum(axis=1, min_count=1)
    return df


def group_internet_understanding(df: pd.DataFrame) -> pd.DataFrame:
    # Groups Internet_Understanding_Score into 5 categories.
    
    bins = [0, 10, 15, 20, 25, 30]
    labels = [
        "Kein Verständnis",
        "Schlechtes Verständnis",
        "Mittelmässiges Verständnis",
        "Gutes Verständnis",
        "Völliges Verständnis",
    ]
    df["Internet Understanding (Grouped)"] = pd.cut(
        df["Internet_Understanding_Score"],
        bins=bins,
        labels=labels,
        include_lowest=True,
    )
    return df


def clean_up_subjects(df: pd.DataFrame, columnname: str, max_subjects: int = 3) -> pd.DataFrame:
    
    def _pick(subjects: list[str], seed_text: str) -> list[str]:
        if len(subjects) <= max_subjects:
            return subjects

        # deterministic pseudo-random order derived from answer text
        digest = hashlib.md5(seed_text.encode("utf-8")).hexdigest()
        seed_int = int(digest[:8], 16)

        # sort by hashed score, then take first max_subjects
        scored = []
        for s in subjects:
            h = hashlib.md5((s + str(seed_int)).encode("utf-8")).hexdigest()
            scored.append((h, s))
        scored.sort(key=lambda x: x[0])

        return [s for _, s in scored[:max_subjects]]

    def _clean(answer):
        if pd.isna(answer):
            return answer
        raw = str(answer).strip()
        if raw == "":
            return answer
        subjects = [s.strip() for s in raw.split(",") if s.strip() != ""]
        chosen = _pick(subjects, raw)
        return ", ".join(chosen)

    df[columnname] = df[columnname].apply(_clean)
    return df

# --------------------------------------------------
# Utilities for cross-tabulations and post-hoc tests
# --------------------------------------------------

def explode_column(df_in: pd.DataFrame, col: str, is_multi: bool) -> pd.DataFrame:
    if col not in df_in.columns:
        return pd.DataFrame(columns=[col])

    tmp = df_in[[col]].dropna().copy()
    tmp[col] = tmp[col].astype("string").str.strip()

    if is_multi:
        tmp[col] = tmp[col].str.split(",")
        tmp = tmp.explode(col)

    tmp[col] = tmp[col].astype("string").str.strip()
    tmp = tmp[tmp[col].notna() & (tmp[col] != "")]
    return tmp


def prepare_pair(
    df_in: pd.DataFrame,
    col_a: str,
    col_b: str,
    a_multi: bool,
    b_multi: bool,
) -> pd.DataFrame:
    a_df = explode_column(df_in, col_a, a_multi)
    if a_df.empty or col_b not in df_in.columns:
        return pd.DataFrame(columns=[col_a, col_b])

    b_series = df_in[col_b].astype("string").str.strip().replace({"": pd.NA})
    data = a_df.join(b_series.rename(col_b), how="inner").dropna(subset=[col_a, col_b])

    if b_multi:
        data[col_b] = data[col_b].astype("string").str.split(",")
        data = data.explode(col_b)
        data[col_b] = data[col_b].astype("string").str.strip()
        data = data[data[col_b].notna() & (data[col_b] != "")]

    return data[[col_a, col_b]]


def order_crosstab(ct: pd.DataFrame, row_var: str, col_var: str) -> pd.DataFrame:
    if row_var in question_orders:
        want = [v for v in question_orders[row_var] if v in ct.index]
        rest = [v for v in ct.index if v not in want]
        ct = ct.reindex(want + rest)
    else:
        try:
            idx_num = pd.to_numeric(ct.index)
            ct = ct.iloc[np.argsort(idx_num)]
        except Exception:
            pass

    if col_var in question_orders:
        want = [v for v in question_orders[col_var] if v in ct.columns]
        rest = [v for v in ct.columns if v not in want]
        ct = ct[want + rest]
    else:
        try:
            _ = [float(c) for c in ct.columns]
            ct = ct[sorted(ct.columns, key=lambda c: float(c))]
        except Exception:
            pass

    return ct

def apply_dummy_spec(df, spec):
    """
    Creates dummy variables from a categorical source column.
    Drops the reference category defined in spec["drop"].
    """
    source = spec["source_column"]
    drop_cat = spec["drop"]
    prefix = spec["prefix"]

    if source not in df.columns:
        return df

    s = df[source].astype("string").str.strip()

    dummies = pd.get_dummies(s, prefix=prefix)
    drop_col = f"{prefix}_{drop_cat}"
    if drop_col in dummies.columns:
        dummies = dummies.drop(columns=[drop_col])

    dummies = dummies.astype("Int64")

    # remove old dummy cols with same prefix if any exist
    existing = [c for c in df.columns if c.startswith(prefix + "_")]
    if existing:
        df = df.drop(columns=existing)

    df = pd.concat([df, dummies], axis=1)
    return df
