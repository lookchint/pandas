def readRFT(path):
    dfRFT = pd.read_excel(path, sheet_name=0, usecols='E:V', skiprows=5, skip_footer=44)
    dfRFT.head(30)
    dfRFT.drop([0], axis=0, inplace=True)
    dfRFT = dfRFT[['TMD_BRT', 'Form_SG']]
    dfRFT.dropna(inplace=True)
    dfRFT.columns = ['DEPT', 'Pressure']
    dfRFT = dfRFT.apply(pd.to_numeric)
    return dfRFT


def readLWD(path):
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
    dfWD = df.apply(pd.to_numeric)
    dfWD = dfWD[['DEPT', 'AT10', 'AT20', 'AT30', 'AT60', 'AT90', 'NPOR', 'GR']]
    return dfWD


def Mergefile(dfRFT, dfWD):
    dfmerge = pd.merge_asof(dfWD, dfRFT, on='DEPT',direction='nearest')
    dfmerge.dropna(inplace=True)
    X = dfmerge[['DEPT', 'AT10', 'AT20', 'AT30', 'AT60', 'AT90', 'NPOR', 'GR']]
    Y = dfmerge['Pressure']
    return dfmerge, X, Y
