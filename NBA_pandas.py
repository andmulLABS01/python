import pandas as pd

#load api_data.csv into dataframe 
df = pd.read_csv("nba_players.csv")

# #print(df)


# #Show the basic statistics of the 'id' column.
# # print(df['id'].describe)

# #Find the number of unique positions in the 'position' column.


# #Rename the column names
# print(df.rename(columns={'id': "Player ID"}, inplace=True))

# # Display the first 5 rows
# print(df.head(6))


# # Filter rows where the 'position' is 'C'
# print(df[df['Position']== 'C'])

# # Sort the DataFrame by 'last_name' in ascending order
# print(df.sort_values(by='Last Name', ascending=True))



# Group the DataFrame by 'team.full_name' and count players in each team
# print(df['Team Name'].value_counts())

# Select specific columns 'first_name' and 'last_name'
# print(df[['First Name', 'Last Name']])


#Create a new column 'full_name' by combining 'first_name' and 'last_name' with a space in between.
# df['Full_name'] = df['First Name'] + ' ' + df['Last Name']
# print(df)

#Show the rows where 'team.full_name' contains the word 'Grizzlies'.