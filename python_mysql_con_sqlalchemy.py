import pandas as pd
import sqlalchemy

name = input('Enter user name: ')
password = input('Enter password: ')
database_name = input('Enter DB name: ')
engine=sqlalchemy.create_engine('mysql+pymysql://'+name+':'+password+'@localhost:3306/'+database_name)
try:
    df= pd.read_sql('show databases',engine)
except sqlalchemy.exc.OperationalError:
    print('connection not established please check given connection details')
    

   
