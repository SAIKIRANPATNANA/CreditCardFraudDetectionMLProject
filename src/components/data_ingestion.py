import os,sys
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from xgboost import XGBClassifier
@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method initiated')
        try:
            df = pd.read_csv(os.path.join('notebooks/data','credit_card_data.csv'))
            logging.info('Dataset read as pandas dataframe')
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)
            logging.info('Starting Train Test Split')
            train_set,test_set = train_test_split(X,y,test_size=0.25,random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info('Data Ingestion is completed')
            return self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path
        except Exception as e:
            logging.info('An Error occured in the Data Ingestion Config')
            return(e,sys)
            
    