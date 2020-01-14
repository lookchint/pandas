import pandas as pd

df_pivot = pd.DataFrame({
    'Mos': ['M', 'O', 'S'],
    'Gun': ['G', 'U', 'N'],
    'Pon': ['P', 'O', 'N']})
print(df_pivot)
print()
print(df_pivot.pivot(index='Mos', columns='Gun'))

df_pivot1 = pd.DataFrame({"height": ['172', '169', '155'],
                          "weight": ['68', '74', '55'],
                          'shoes': ['41', '42', '36']})
print(df_pivot1)
print(df_pivot1.pivot(index='shoes', columns='weight'))

import matplotlib.pyplot as plt


plt.show()