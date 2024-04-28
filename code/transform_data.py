import os as os
import pandas as pd
import numpy as ny

os.chdir("/Users/i554234/uni/pein/course_project/data")

sheet_list = ['pavlovo', 'drujba', 'hipodruma']

dtype_dict_day_file = {'Date': str, 'O3': float, 'RM10': float}
usecols_day_file = ['Date', 'O3', 'RM10'] #nadejda is missing pressure, mladost is missing O3, orlov is missing 03

dtype_dict_hour_file = {'Date': str, 'NO': float, 'NO2': float, 'AirTemp': float, 'Press': float, 'UMR': float}
usecols_hour_file = ['Date', 'NO', 'NO2', 'AirTemp', 'Press', 'UMR']

day_file = pd.read_excel('day.xls',
                        sheet_name=sheet_list,
                        header=1, 
                        usecols=usecols_day_file, 
                        dtype=dtype_dict_day_file,
                        )

hour_file = pd.read_excel('hour.xls',
                        sheet_name=sheet_list, 
                        header=1, 
                        usecols=usecols_hour_file, 
                        dtype=dtype_dict_hour_file,
                        )

merged_df = pd.DataFrame()
for sheet_name, day_data in day_file.items():
    for i in range(day_data['Date'].size):
        date = day_data.iloc[i]['Date']
        o3 = day_data.iloc[i]['O3']
        rm10 = day_data.iloc[i]['RM10']

        hour_sheet_data = hour_file[sheet_name]
        filtered_hour_file = hour_sheet_data[hour_sheet_data['Date'].str.contains(date)]
        filtered_hour_file.insert(2, 'O3', o3)
        filtered_hour_file.insert(3, 'RM10', rm10)

        merged_df = merged_df._append(filtered_hour_file, ignore_index=True)

merged_df = merged_df.dropna()
rounded_merged_df = merged_df.round({'NO': 2, 'NO2': 2, 'O3': 2, 'RM10': 2, 'AirTemp': 1, 'UMR': 1, 'Press': 0})
rounded_merged_df.to_csv('/Users/i554234/uni/pein/course_project/data/data.csv', columns = ['NO', 'NO2', 'AirTemp', 'Press', 'UMR', 'O3', 'RM10'])