"""
You can run this example like this:
    .. code:: console
            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler
If that does not work, see :ref:`CommandLine`.
"""
import luigi
import numpy as np
import pandas as pd
import datetime as dt
import time
import pickle
from sklearn.preprocessing import Imputer, StandardScaler
import scipy
import nltk
nltk.download('brown')
nltk.download('punkt')
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import pickle

import boto3
import botocore
import argparse
import sys
import datetime
from luigi.parameter import MissingParameterException

import os



class S3_DataIngestion(luigi.Task):
	akey=luigi.Parameter()
	skey=luigi.Parameter()
	def requires(self):
		return None

	def run(self):
		akey=luigi.Parameter()
		skey=luigi.Parameter()
		aws_access_key_id = akey
		aws_secret_access_key = skey

		s3 = boto3.resource('s3')
		buckname="finalprojectabg"
		client = boto3.client('s3','us-west-2',aws_access_key_id=self.akey,aws_secret_access_key=self.skey)
		i = 0
		for k in client.list_objects(Bucket=buckname)['Contents']:
			if "scraped" in k['Key']:
				print(k['Key'])
				key = k['Key']
				client.download_file(buckname, key, 'scraped/'+str(i)+".json")
				i=i+1
		q = pd.DataFrame()
		u = 1
		for k in os.listdir(os.getcwd()+"/scraped"):
			if(u!=1):
				print('scraped/'+str(k))
				r = pd.read_json("./scraped/"+str(k), lines=True)
				print(r)
				q = q.append(r)
				print(q)
			else:
				r = pd.read_json("./scraped/"+str(k), lines=True)
				q=r.copy()
			u=u+1
		q.to_json(self.output().path, orient="records")

	def output(self):
		return luigi.LocalTarget("online.json")

class Train_DataIngestion(luigi.Task):
	def requires(self):
		return None
	def run(self):
		trainingData= pd.read_csv("../smartresume/static/data/raw/data_job_posts.csv")
		trainingData.to_csv(self.output().path, index=False)
	def output(self):
		return luigi.LocalTarget("data_job_posts.csv")

# ### Drop unnecessary columns. 
# So here we need to predict the longitude and latitude of GPS, which can be done using the WAP columns. 
# Data Cleaning and processing

class DataPreProcessing(luigi.Task):
	akey=luigi.Parameter()
	skey=luigi.Parameter()
	def requires(self):
		yield Train_DataIngestion()
		yield S3_DataIngestion(akey=self.akey, skey=self.skey)


	def run(self):
		fb = pd.read_csv(Train_DataIngestion().output().path)
		f2 = pd.read_csv(S3_DataIngestion(akey=self.akey, skey=self.skey).output().path)
		trainingData = fb
		print("In Data Pre Processing")
		profiles = ["Software Developer","Web Developer","Java Developer","System Administrator","Software Engineer","QA Engineer","PHP Developer","Senior Software Engineer","Programmer","IT Specialist","Web Designer","Android Developer","C++ Software Developer","Python Developers","Data Analyst"]

		select_position = trainingData.loc[trainingData['Title'].isin(profiles)]
		train = select_position[['jobpost','Title']]
		cl = NaiveBayesClassifier(train.values)
		cl_model = cl
		outFile = open(self.output().path, 'wb')
		pickle.dump(cl_model, outFile, protocol=pickle.HIGHEST_PROTOCOL)
		outFile.close()
		file = open(self.output().path, 'wb') #tried to use 'a' in place of 'w' ie. append
		pickle.dump(cl_model,file)
		file.close()
		file = open("../smartresume/static/models/model.pkl", 'wb') #tried to use 'a' in place of 'w' ie. append
		pickle.dump(cl_model,file)
		file.close()

	def output(self):
		return luigi.LocalTarget('model.pkl')

class uploadmodeltos3(luigi.Task):
	akey=luigi.Parameter()
	skey=luigi.Parameter()
	def requires(self):
		yield DataPreProcessing(akey=self.akey, skey=self.skey)
	def run(self):
		if str(self.akey) == "1" or str(self.skey) == "1":
			print("Enter the AWS keys and try again")
			sys.exit()
		
		s3 = boto3.resource('s3')
		buckname="finalprojectabg"
		client = boto3.client('s3','us-west-2',aws_access_key_id=self.akey,aws_secret_access_key=self.skey)
		# client.create_bucket(Bucket=buckname,CreateBucketConfiguration={'LocationConstraint':'us-west-2'})
		client.upload_file('model.pkl', buckname, 'model.pkl')

#lskdjflskfdj
if __name__=='__main__':
	try:
		luigi.run()

	except MissingParameterException:
		print("Please provide Access Keys and Secret Access Keys")
		sys.exit()