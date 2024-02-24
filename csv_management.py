import pandas as pd 
import zipfile

# read a csv file from a website (since it is a zip of many csv files ...)


zip_url = 'https://www.football-data.co.uk/mmz4281/2324/data.zip'
zip_file = 'data.zip'

# Download the ZIP file
import urllib.request
urllib.request.urlretrieve(zip_url, zip_file)

# Extract the CSV files from the ZIP file
csv_files = []
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    csv_files = zip_ref.namelist()  # Get the list of all file names in the ZIP file
    zip_ref.extractall()

# Read the CSV files
print(len(csv_files)) # 22
print(csv_files)
file = pd.read_csv(csv_files[3])

# showing dataframes
print(file.head())

""" 
 Div        Date   Time     HomeTeam       AwayTeam  FTHG  ...  PCAHH PCAHA  MaxCAHH  MaxCAHA AvgCAHH AvgCAHA
0  E0  11/08/2023  20:00      Burnley       Man City     0  ...   1.95  1.97      NaN      NaN    1.92    1.95
1  E0  12/08/2023  12:30      Arsenal  Nott'm Forest     2  ...   1.93  1.97     2.01     2.09    1.95    1.92
2  E0  12/08/2023  15:00  Bournemouth       West Ham     1  ...   2.01  1.92     2.06     1.96    1.96    1.91
3  E0  12/08/2023  15:00     Brighton          Luton     4  ...   2.00  1.91     2.14     1.93    2.00    1.86
4  E0  12/08/2023  15:00      Everton         Fulham     0  ...   2.04  1.88     2.08     1.99    1.98    1.88

[5 rows x 106 columns]
"""
print(file.columns)

""" 
Index(['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR',
       'HTHG', 'HTAG',
       ...
       'AvgC<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'PCAHH', 'PCAHA', 'MaxCAHH',
       'MaxCAHA', 'AvgCAHH', 'AvgCAHA'],
      dtype='object', length=106)
"""

