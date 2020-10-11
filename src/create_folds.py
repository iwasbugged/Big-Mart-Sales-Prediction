# create_folds.py
import numpy as np 
import pandas as pd 

from sklearn import model_selection
from sklearn import preprocessing

def create_folds():
    # read dataset
    df = pd.read_csv('../dataset/train.csv')
    # creating a column name fold and fill it with -1
    df['Fold'] = -1
    # shuffling the data
    df = df.sample(frac = 1).reset_index(drop = True)

    # since the problem is regression type and the distribution of the data is not normal
    # hence we will use StratifiedKFold for the cross validation and in order to do that 
    # first we need the create a bin for the column called "Item_Outlet_Sales"
    num_bins = np.floor(1 + np.log2(len(df))).astype(int)
    df["Bins"] = pd.cut(df['Item_Outlet_Sales'] , bins = num_bins , labels = False)

    # initializing the StratifiedKFolds
    kf = model_selection.StratifiedKFold(n_splits= 5)

    # fill the fold column
    for f, (t_ , v_) in enumerate(kf.split(X = df ,y= df['Bins'])):
        df.loc[v_ , 'Fold'] = f

    # droping column "Bins" and saving the dataset with fold column
    df = df.drop('Bins' , axis = 1)
    df.to_csv('../dataset/train_folds.csv', index = False)

if __name__ == "__main__":
    create_folds()