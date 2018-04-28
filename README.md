# Final Project

Luigi Link - http://ec2-52-32-210-114.us-west-2.compute.amazonaws.com:8082/

Project Link - http://ec2-52-32-210-114.us-west-2.compute.amazonaws.com:8000/

# Steps to execute docker
docker run -it -p 8000:8000 -p 8082:8082 sreeragsreenath/finalads
cd mlbcsite/
python3 sunprocess.py "aws s3 id" "aws s3 key"

## Introduction

MLBC is a Web based platform for candidates who are seeking a job and recruiter who are looking for the right talent. The platform scrapes and analyzes publicly available job posting data from sites like Glassdoor, LinkedIn, etc. The system will recommend the candidate which job title will fit him/her based on their resume. The system will also give job links to the application form. The platform will also help us to gain statistical information about the latest job trend.

 
## Stakeholders
The Supervising authority
The Supervising authority is a person that governs the entire system.  Having supervisory powers over some aspects of management decision-making. Basically  a person with more power than others.
The Beneficiaries (or users)
The beneficiaries (or users) are all natural persons or corporate body, students , recipients of the services provided by MBCS.

The Recruiters 
A person whose job is to enlist or enroll people as employees as members of an organization.


The steps involved

We have used an existing dataset provided by Kaggle
DataSet : 
Scrapped information and skill sets from websites such as Indeed
This will be done by giving the url  as input to a web scraper
Library such as scrapy will be used to run multiple web crawlers on a single website to  optimise scrapping process
Analysing the data and segregating the content to skills and tools mandatory and the expertise level
The data is stored in SQLite database supported by Django server for further processing
We tried out different machine learning models and hybrid techniques to optimise     the result
Made a web based application to interact with the system through which the user can upload his/her data.
The web based application and the authentication is done using python Django. 
The Web application allows the user to upload the document and it will Parse the users resume and scrape relevant information i.e. tools, skills, location, work experience and serve it as parameters for our prediction model.
After the model is executed, it will output “Best suited position” according to his/her resume along with Ranking. It also outputs latest Job postings where the user can apply. 
The entire process is pipelined using LUIGI.
We have deployed the Django application on EC2 server and storing and retrieving the model from Amazon S3.
Finally we have dockerized the entire application, so a person with any operating system can simply pull the docker image and run it on his own machine. 


Project Tools:
Language : Python 
Pipeline : Luigi
Framework : Django
Databse : SQL
Tools used: Jupyter Notebooks and Docker , Xamp. 

Libraries Used :- 
Django
PyPDF2
NLTK
TextBlob
Boto3


Exploratory Data Analysis 
Conduct EDA using Python libraries - 
Seaborn, Numpy, MissingNo, Pickle, Plotly, Pandas, Scipy, Sklearn, Matplotlib			


### INFO
1. Language used : Python
2. Process Followed : Data Ingestion, Data Wrangling, Exploratory Data Analysis
3. Tools used :  Jupyter Notebook

## Conclusion

Our website will show you the Preferred Job Postings as well as the Positions one should apply.


