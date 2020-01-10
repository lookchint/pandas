import pandas as pd
from function import Append


dftbl1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [1, 2, 3, 4]})
dftbl2 = pd.DataFrame({'A': [2, 3, 5, 6], 'C': ['ก', 'ข', 'ค', 'ง']})

x=Append(dftbl1, dftbl2)
print(x)