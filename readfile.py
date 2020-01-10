import pandas as pd
import os, sys
from os.path import dirname


def readwelllog(path):
    with open(path, 'r') as f:
        is_curve_section = False
        is_ascii_section = False
        log = []
        headers = []
        for line in f:
            if '~Parameter' in line:
                is_curve_section = False
            if is_curve_section:
                headers.append(line.split(':')[1].strip())
            if is_ascii_section:
                log.append(line.replace('  ', ' ').strip().split(' '))
            if '~Ascii' in line:
                is_ascii_section = True
            if '~Curve' in line:
                is_curve_section = True

    df = pd.DataFrame(log, columns=headers)
    df['WELL_ID'] = os.path.split(path)[1]
    return df
