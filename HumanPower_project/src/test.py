# libraries
import os
import pandas as pd

# create path
path_in = r'C:\Users\Lavy Ngo\Desktop\CS5530\Assignment1\HumanPower_project\data_raw\raw_human_data.csv'
path_out = r'C:\Users\Lavy Ngo\Desktop\CS5530\Assignment1\HumanPower_project\data_clean\clean_human_data.csv'

# read data from a raw file
data = pd.read_csv(path_in)
print(data)
print()

# find unique value each column
for col in data:
    print(data[col].unique())
print()

# rename some of the header for better spacing
data = data.rename(columns={'Height (Inches)': 'Height/inches',
                            'Weight (Pounds)': 'Weight/lbs',
                            'Grip strength': 'Grip/strength'})
print(data)
print()

# using filter to eliminate all of the weak ones, and keep 'strong' ones
filter = data["Frailty"] == "N"
new_data = data[filter]
print(new_data)

# write new_data the cleaned csv file
new_data.to_csv(path_out)
