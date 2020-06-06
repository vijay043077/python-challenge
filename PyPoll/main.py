# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# dependencies
import csv
import os
import sys


# %%
# set file path
csv_path = os.path.join("..", "PyPoll", "election_data.csv")
csv_path


# %%
# set variables for first row
vote_count = {}
candidates = []


# %%
# CSV reader specifies delimiter and variable that holds contents
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for row in csv_reader:
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            vote_count[candidate] = 1
        else:
            vote_count[candidate] = vote_count[candidate]+1

total_votes = sum(vote_count.values())

print(f'Total Votes: {total_votes}')
print('----------------------')


# %%

