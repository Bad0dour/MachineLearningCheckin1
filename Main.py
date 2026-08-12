import pandas as pd

runs = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]    # week numbers
members = ["Daniel Richard", "Ben Kelly", "James Ford", "Oliver Bixler", "Frederick Stevens"]  # player names
times = [ # Runners times (s) for each race
    [301,274,253,256,247],  # Daniel
    [253,242,237,None,202], # Ben
    [304,281,293,276,265],  # James
    [202,None,195,196,204], # Oliver
    [261,270,252,238,180],  # Frederick
]

df = pd.DataFrame(times, columns=runs, index=members)  # creates dataframe with the times as the elements, week numbers as columns, and members as rows
print(df)     # print dataframe

runner_data = {}      # Creates empty dict
for name in members:    # loops through each player
    runner_data[name] = df.loc[name].tolist()   # adds each player to the dict with key as name and value as their times (the to_list() removes metadata such as week headers)
    print(runner_data[name])       # prints each players dict key/value

print(runner_data)   # prints finished dictionary
print("\n     Player Time Averages:")
print(df.mean(axis=1).to_string())  # The to_string() simply removes the 'dtype: float64' at the bottom.
