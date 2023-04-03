from datetime import datetime
from csv import reader
from pyspark import SparkContext

sc = SparkContext(appName="hw2") 
sc.setLogLevel("ERROR")

# Read input data from HDFS to create an RDD
data = sc.textFile("hdfs://group8-1:54310/hw1-input/")
header = data.first() 
# Filter out header
data = data.filter(lambda row : row != header)

# Use csv reader to split each line of file into a list of elements. # this will automatically split the csv data correctly.
splittedData = data.mapPartitions(lambda x: reader(x))

# Use filter to select only those rows in which crime type is not blank
splitData = splittedData.filter(lambda x: x[7])

# Getting location of most of crime happening in NYC.
city = splitData.map(lambda x: x[13])
most_happening_crime = city.map(lambda x: (x,1)).reduceByKey(lambda a,b: (a +b)).sortBy(keyfunc=lambda x: x[1],ascending=False).take(1)

# July crime data
july_crime = splittedData.filter(lambda x: datetime.strptime(x[5], '%m/%d/%Y').month == 7)

# Getting top 3 crime in July
top_crime_july=july_crime.map(lambda x:(x[7],1)).reduceByKey(lambda a,b: (a+b)).sortBy(keyfunc=lambda x:x[1] ,ascending=False).take(3)

# Getting the number of crimes of type "DANGEROUS WEAPONS" reported in July
crime_by_wep_july= july_crime.filter(lambda x: x[7] == 'DANGEROUS WEAPONS').count()

# Printing the information
print("\nThe location where most of the crime is happening in New York as well as the total in that location are:")
print(most_happening_crime)

print("\nThe top 3 crimes reported in July along with their total:")
print(top_crime_july)

print("\nNumber of DANGEROUS WEAPONS crimes that were reported in the month of July is: ")
print(crime_by_wep_july)