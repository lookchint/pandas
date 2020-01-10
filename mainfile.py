import pandas as pd
from function import Append, Merge, Pivottbl
from readfile import readwelllog
from os.path import join, dirname

dftbl1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [1, 2, 3, 4]})
dftbl2 = pd.DataFrame({'A': [2, 3, 5, 6], 'C': ['ก', 'ข', 'ค', 'ง']})
inner = "inner"
path = join(dirname(__file__), 'AT-33-F_SX(TCombo)_6.125_ULog_Envi.las')
#print(path)
#print(path)
appendtbl = Append(dftbl1, dftbl2)

mergetbl = Merge(dftbl1, dftbl2, inner)
# print(mergetbl)
readwelllog(path)
print(readwelllog(path))
