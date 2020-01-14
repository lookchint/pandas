import pandas as pd



def readRFT(pathRFT):
    dfRFT = pd.read_excel(pathRFT, sheet_name=0, usecols='E:V', skiprows=5, skip_footer=44)
    dfRFT.drop([0], axis=0, inplace=True)
    dfRFT = dfRFT[['TMD_BRT', 'Form_SG']]
    dfRFT.dropna(inplace=True)
    dfRFT.columns = ['DEPT', 'Pressure']
    dfRFT = dfRFT.apply(pd.to_numeric)
    return dfRFT


def readLWD(pathLWD):
    import re
    with open(pathLWD, encoding="ISO-8859-1") as f:
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
    dfLWD = df.apply(pd.to_numeric)
    dfLWD = dfLWD[['DEPT', 'AT10', 'AT20', 'AT30', 'AT60', 'AT90', 'NPOR', 'GR']]
    return dfLWD


def Mergefile(dfRFT, dfLWD):
    dfmerge = pd.merge_asof(dfRFT, dfLWD, on='DEPT', direction='nearest')
    dfmerge

    # X = dfmerge[['DEPT', 'AT10', 'AT20', 'AT30', 'AT60', 'AT90', 'NPOR', 'GR']]
    # Y = dfmerge['Pressure']
    return dfmerge
