from __future__ import print_function
import pandas as pd
import numpy as np
data_dict = {'CHECKPOINTS': [None, 'DATE', 'SHIFT', 'TIME', 'OP25Cl', 'OP25JG', 'OP25FX', 'OP30ES', 'OP25TH', 'OP25LC', 'OP20AP', 'OP30MC', 'OP30FX', 'OP30SC', 'OP30ID', 'OP30PM', 'OP30EMP'],
 'value1': [None, '11-02-2022', 'A', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '5.400000E+0', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'],
  'value2': [None, '11-02-2022', 'B', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '   5.400000E+1', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'],
   'value3': [None, '11-02-2022', 'C', '02.09.21_PM', 'OK', 'Ofty', 'OK', 'OK', 'OK', 'OK', '   5.400000E+2', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'], 
   'value4': [None, '11-02-2022', 'A', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '   5.400000E+3', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'], 
   'value5': [None, '11-02-2022', 'B', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '   5.400000E+4', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'],
    'value6': [None, '11-02-2022', 'A', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '   5.400000E+5', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini'],
     'value7': [None, '11-02-2022', 'B', '02.09.21_PM', 'OK', 'OK', 'OK', 'OK', 'OK', 'OK', '   5.400000E+6', 'OK', 'OK', 'OK', 'OK', 'OK', 'thatchayini']}
df=pd.DataFrame(data_dict)
df.head()
from weasyprint import HTML
HTML(string='asd').write_pdf("report.pdf")
