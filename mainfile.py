import pandas as pd

pathRFT = 'AT-33_F_PTW_6.125''.xls'
pathLWD = "AT-33-F_SX(TCombo)_6.125_DLog_Envi.las"
dataRFT = readRFT(pathRFT)
dataLWD = readLWD(pathLWD)
Mergefile(dataRFT, dataLWD)
