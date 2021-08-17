import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from acquire import get_iris_data, get_titanic_data


def prep_iris():
    df = get_iris_data()
    df_iris = df.drop(columns = ['species_id', 'measurement_id'])
    df_iris.rename(columns={"species_name": "species"}, inplace = True)
    df_dummy = pd.get_dummies(df_iris[['species']])
    df_final = pd.concat([df_iris, df_dummy], axis = 1)
    return df_final