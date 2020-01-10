import pandas as pd


def Append(dftbl1, dftbl2):
    dfappend = dftbl1.append(dftbl2, ignore_index=True)
    return dfappend


def Merge(dftbl1, dftbl2, howtojoin):
    dfmerge = pd.merge(dftbl1, dftbl2, left_on="A",
                       right_on="A", how=howtojoin)
    return dfmerge


def Pivottbl(dftbl1, row, cols):
    dfpivot = dftbl.pivot_table(index=row, columns=cols, values='A')
    return dfpivot


def Melt(dftbl1, rows):
    dfmelt = dftbl1.pivot_table(index=rows)
    return dfmelt
