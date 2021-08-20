import pandas as pd
import os
from env import host, user, password
def get_db_url(host = host, user = user, password = password, db = 'employees'):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_db_url(db = 'titanic_db'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)
        # Return the dataframe to the calling code
        return df


def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(
        '''SELECT
            m.measurement_id,
            m.sepal_length,
            m.sepal_width,
            m.petal_length,
            m.petal_width,
            m.species_id,
            s.species_name
        FROM measurements as m
        JOIN species AS s 
        USING(species_id)''', 
            get_db_url(db = 'iris_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  
print(get_iris_data())

def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('SELECT * FROM customers', get_db_url(db = 'telco_churn'))
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)
        # Return the dataframe to the calling code
        return df