import pandas as pd
import jointbl

pathRFT = "AT-33_F_PTW_6.125''.xls"
pathLWD = 'AT-33-F_SX(TCombo)_6.125_DLog_Envi.las'
readRFT =jointbl.readRFT(pathRFT)

#dfLWD = readLWD(pathLWD)
#dfMerge = Mergefile(dfRFT, dfLWD)
#X = dfMerge[['DEPT', 'AT10', 'AT20', 'AT30', 'AT60', 'AT90', 'NPOR', 'GR']]
#Y = dfMerge[['Pressure']]
