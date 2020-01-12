def merge_output():
    # -*- coding: utf-8 -*-
    import csv
    import pandas as pd
    columns = ['Product','edition','price','location','OS','state','carrier','color','storage','condition','listed_date','views','user','url']
    n_columns = len(columns)
    output_inc = pd.read_csv('output.csv', delimiter=',',header=None,skiprows=1)
    print("New listings -",len(output_inc))
    output_main = pd.read_csv('output_main.csv',delimiter=',',header=None,skiprows=1)
    print("Main listing -",len(output_main))
    new_output_main = pd.concat([output_main, output_inc],  axis=0)
    new_output_main.columns=columns
    new_output_main.drop_duplicates(subset='url', keep="last", inplace=True)
    print("Combined listings -",len(new_output_main))
    new_output_main.to_csv('output_main.csv', index=False)
