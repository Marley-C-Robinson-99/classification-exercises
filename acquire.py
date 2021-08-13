import pandas as pd
import os
from env import host, user, password
from pydataset import data
def get_db_url(host = host, user = user, password = password, db = 'employees'):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_db_url(db = 'titanic_db'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  
get_titanic_data()

def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM species', get_db_url(db = 'iris_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  

get_iris_data()

