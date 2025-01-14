# In this exercise, you have monthly stock data for four companies 
# downloaded from Yahoo Finance (http://finance.yahoo.com/). The data is stored as one row 
# for each company and each column is the end-of-month closing price. 
# The file name is given to you in the variable file_messy.

# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)