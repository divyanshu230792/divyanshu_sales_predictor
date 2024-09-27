import pickle
import json
import config
import numpy as np
import pandas as pd

class Get_Sales():
    def __init__(self):
        pass

    def load_data(self):
        with open(config.MODEL_FILENAME,'rb') as f:
            self.lr_sales=pickle.load(f)

        with open(config.COLUMN_DATA,'r') as  f:
            self.col_data=json.load(f)

        self.col_names=self.lr_sales.feature_names_in_
        self.col_count=self.lr_sales.n_features_in_

    def get_sales_predictor(self,TV, Radio,Social_Media,Influencer):
        self.load_data()
        Influencer=self.col_data['Influencer'][Influencer]
        test_array=np.zeros((1,self.col_count))
        test_array[0][0]=TV
        test_array[0][1]=Radio
        test_array[0][2]=Social_Media
        test_array[0][3]=Influencer
        sales_predict=self.lr_sales.predict(test_array)[0]
        return sales_predict

def load_dataset():
    df=pd.read_csv(config.CSV_FILENAME)
    return df
       




