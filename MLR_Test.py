import pandas as pd

path = 'file/AT-33-F_SX(TCombo)_6.125_ULog_Envi.las'
import re

with open(path, encoding="ISO-8859-1") as f:
    header_section = False
    data_section = False
    headers = []
    data = []
    for line in f:
        if header_section and ('~' in line):
            header_section = False

        if '~curve information' in line.lower():
            header_section = True

        if '~A' in line:
            data_section = True

        if header_section and ('#' != line[0]) and ('~' != line[0]):
            headers.append(line.split()[0].split('.')[0].strip())

        if data_section and ('#' != line[0]) and ('~' != line[0]):
            data.append(re.split('\s+', line.strip()))

df = pd.DataFrame(data, columns=headers)
df = df.apply(pd.to_numeric)

print(df)
