# import boto3
# import botocore
# import argparse
# import sys
# import datetime
# from luigi.parameter import MissingParameterException

# import os
# aws_access_key_id = "AKIAJX47MRD5AYURRMHA"
# aws_secret_access_key = "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"

# s3 = boto3.resource('s3')
# buckname="finalprojectabg"
# client = boto3.client('s3','us-west-2',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
# y = os.listdir(os.getcwd()+"/scraped")
# i = 0
# for k in client.list_objects(Bucket=buckname)['Contents']:
# 	print(k['Key'])
# 	key = k['Key']
# 	client.download_file(buckname, key, "scraped/"+str(i)+".json")
# 	i=i+1
# # key = client.list_objects(Bucket=buckname)['Contents'][2]['Key']
# # 

import pandas as pd
import os
# r = pd.read_json("file://scraped/0.json")
# print(r)

# q = pd.DataFrame()
# u = 1
# for k in os.listdir(os.getcwd()+"/scraped"):
# 	if(u!=1):
# 		print('scraped/'+str(k))
# 		r = pd.read_json("./scraped/"+str(k), lines=True)
# 		print(r)
# 		q = q.append(r,ignore_index=True)
# 		print(q)
# 	else:
# 		r = pd.read_json("./scraped/"+str(k), lines=True)
# 		q=r.copy()
# 	u=u+1
# print(q)
# q.to_json("online.json", orient="records")
r = pd.read_csv("./scraped/"+str(k), lines=True)