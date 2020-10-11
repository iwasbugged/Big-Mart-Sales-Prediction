# train.py
import pandas as pd 
import numpy as np
from sklearn import preprocessing


def run(df , fold):
    import feature_generator

    # reading training data
    #df_train = pd.read_csv('../dataset/train_folds.csv')

    # seperating the categorical column from the numerical columns
    cat_cols = [
       c for c in df.columns.to_list() if df[c].dtypes == np.object
    ]
    # separating numerical columns from the rest of the columns
    num_cols = [
        c for c in df.columns if c not in cat_cols
    ]

    # lets make a list of column which we have to combine for the feature generation
    comb_cols = [
        c for c in cat_cols if c not in ( 'Outlet_Identifier')
    ]

    df , cat_cols = feature_generator.feature_engineering(df , comb_cols)

    return df



if __name__ == '__main__':
    df = pd.read_csv('../dataset/train_folds.csv')
    df = run(df , 1)
    print(df.head())
