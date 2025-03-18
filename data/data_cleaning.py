import pandas as pd
import openpyxl


pwt = pd.read_excel('C:\\Users\\333702\\Documents\\edu_growth_diss\\data\\pwt_data.xlsx')
wdi = pd.read_excel('C:\\Users\\333702\\Documents\\edu_growth_diss\\data\\wdi_data.xlsx')
oecd = pd.read_excel('C:\\Users\\333702\\Documents\\edu_growth_diss\\data\\oecd_list.xlsx')

print(pwt)
print(wdi)
print(oecd)

# long format wdi
wdi_melted = pd.melt(wdi, id_vars=['Country', 'Series Name'], var_name='Year', value_name='Value')
wdi_pivoted = wdi_melted.pivot_table(index=['Country', 'Year'], columns='Series Name', values='Value').reset_index()

# combine and filter for oecd only
merged_data = pd.merge(wdi_pivoted, pwt, on=['Country', 'Year'], how='left')
oecd_countries = oecd['Country'].tolist()
filtered_data = merged_data[merged_data['Country'].isin(oecd_countries)]

print(filtered_data)
filtered_data.to_excel('data/filtered_data.xlsx', index=False)
filtered_data.to_csv('data/filtered_data.csv', index=False)