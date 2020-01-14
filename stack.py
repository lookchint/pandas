import pandas as pd
import seaborn as sns

import config

multicolumns = pd.MultiIndex.from_tuples([['height', 'cm'],
                                          ['weight', 'kg'],
                                          ['feet', 'inches']])
df = pd.DataFrame([[169, 74, 41],
                   [172, 68, 42],
                   [155, 500, 90]],
                  index=['Mos', 'Gun', 'Pound'],
                  columns=['height', 'weight', 'feet'])
# df_multicol = pd.DataFrame([[169, 74, 41],
#                    [172, 68, 42],
#                    [155, 500, 90]],
#                   index=['Mos', 'Gun', 'Pound'],
#                   columns=multicolumns)
print(df)
print()
print(df.stack)
# print()
# print(df.stack(0))
# print()
# print(df.stack([0, 1]))
# print()
# print(df.stack(0, dropna=True))
# print()


df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]],
                                    index=['cat', 'dog'],
                                    columns=['weight', 'height'])
print(df_single_level_cols)
