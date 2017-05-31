import urllib
import os

string = 'DRIVER=/usr/local/lib/libtdsodbc.so;' + \
    'SERVER=atlas-bi-slave;PORT=1433;' + \
    'DATABASE=ODS;' + \
    'UID={0};' + \
    'PWD={1};' + \
    'TDS_Version=7.1'
string = string.format(os.environ['RV_USER'], os.environ['RV_PASS'])
quoted = urllib.quote_plus(string)    
print 'mssql+pyodbc:///?odbc_connect={quoted}'.format(quoted=quoted)