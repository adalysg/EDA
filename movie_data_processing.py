# Goal: parse Genre col into list, iterate and compare with cols that have null Revenue vals, to take the avg and substitute

import pandas as pd
import numpy as np

def partial_match_mean(row, exact_means):
    # row = row of interest, to be iteratred
    # exact_means = target rows (don't have null Revenue vals) -> means of matched genres already determined

    if pd.notna(row["Revenue (Millions)"]): # if val not null, keep (no action needed)
        return row["Revenue (Millions)"]

    curr_genre = set(row["Genre"].split(","))
    partial_matches = []

    for target_genre, mean_val in exact_means.items():
        target_genre_set = set(target_genre.split(","))

        if curr_genre & target_genre_set:
            partial_matches.append(mean_val)

        return np.mean(partial_matches) if partial_matches else np.nan

# partial_match_mean decreases num of null Revenue rows from 128 to 111