## old - this is python2
from sqlalchemy import create_engine
import os
pwd = os.environ['PWD']
engine = create_engine()
con = engine.connect()
con
engine.driver
engine.table_names('ODS', con)
dir(engine)


engine = create_engine("mssql+pyodbc://REDVENTURES\jizzard:" + pwd + "@atlas-bi-slave:1433/ODS?driver=/usr/local/lib/libtdsodbc.so")
ec = engine.connect()
dir(ec)
ec._connection_is_valid

with engine.connect() as con:
    rs = con.execute('select top 10 * from PipelineIntegration.dbo.MessageEnvelope')
    for row in rs:
        print row