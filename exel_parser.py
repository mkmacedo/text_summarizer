import xlrd
import csv
import pandas as pd

from text_summarizer import Summarizer

df = pd.read_excel(r'rel.xlsx')

df.to_csv('rel.csv', index=None, header=True)

for i in range(50):
    s = Summarizer(df.loc[i,'Descrição da reclamação'])
    print(s.summary())
    print()

#work_book = xlrd.open_workbook('rel.xls', on_demand=True)
#worksheet = workbook.sheet_by_index(0)

#print(worksheet.cell(0,0))

