import pandas as pd


#===========================

data=pd.read_csv('data/Expresso_churn_dataset.csv')

#====================

data[['REGION','TOP_PACK']]=data[['REGION','TOP_PACK']].fillna('unknown')
data[['FREQUENCE','TIGO','ZONE1','ZONE2','DATA_VOLUME','MONTANT','FREQUENCE_RECH','REVENUE','ARPU_SEGMENT','ON_NET','ORANGE','FREQ_TOP_PACK']]=data[['FREQUENCE','TIGO','ZONE1','ZONE2','DATA_VOLUME','MONTANT','FREQUENCE_RECH','REVENUE','ARPU_SEGMENT','ON_NET','ORANGE','FREQ_TOP_PACK']].fillna(000)


#================

data.drop(columns=['user_id','ARPU_SEGMENT'],inplace=True,axis=1)

#===========

data.to_csv('data/expresso_feature_engineering.csv',index_label=False)

