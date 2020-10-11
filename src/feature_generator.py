# feature_engineering.py
import numpy as np
import pandas as pd 
import itertools


def feature_engineering(df , cat_feats= None , num_feats= None):
    '''
    This function is for feature extraction from the "Big Mart Sales Prediction"
    '''
    map_dict = {
        'Low Fat' : 'Low Fat',
        'LW' : 'Low Fat',
        'low fat' : 'Low Fat',
        'Regular' : 'Regular',
        'reg' : 'Regular'
    }
    df.loc[: , 'Item_Fat_Content'] = df['Item_Fat_Content'].map(map_dict)

    # creating a column "MRP_Per_Unit" which is "Item_MRP" / "Item_Weight"
    df.loc[ : , 'MRP_Per_Unit'] = df['Item_MRP'] / df['Item_Weight']

    # Since the latest Outlet estabilished in 2009 so let make it refrence for the calculating
    # year of establishment
    df.loc[: , 'Year'] = 2009 - df['Outlet_Establishment_Year'].values

    # Let's combine categorical features in two pairs
    combi = list(itertools.combinations(cat_feats , 2))
    for c1 , c2 in combi:
        cat_feats.append(c1+"_"+c2)
        df.loc[
            : , c1+"_"+c2
        ] = df[c1].astype(str)+'_'+df[c2].astype(str)

    return df, cat_feats