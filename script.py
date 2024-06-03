import pandas as pd

# Create a DataFrame with the required columns and a sample entry
data = {
    "Problem": ["Example Problem"],
    "Date Solved": ["2024-06-01"],
    "Repeat Date": [""],  # This will be calculated with a formula in Excel
    "Link": ["https://leetcode.com/problems/example-problem"]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file with the formula for "Repeat Date"
excel_path = "/LeetCode_Tracking_Clean.xlsx"

# Write to Excel, adding the formula to the "Repeat Date" column
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    worksheet = writer.sheets['Sheet1']
    worksheet.write('C1', 'Repeat Date')
    worksheet.write_formula('C2', '=B2 + 10')
    worksheet.set_column('A:D', 30)  # Adjust column width for better readability

excel_path
