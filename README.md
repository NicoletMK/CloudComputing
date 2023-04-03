# Setup
This project is build on Linux OS. 

Setup a Hadoop cluster consisting of 2 VMs in the Chameleon cloud and start the Hadoop daemon processes.

# Data Mining
Download the New York City Crime Data on master VM as follows: wget http://cs.utsa.edu/~plama/CS4843/NYPD_Complaint_Data_Current_YTD.csv

# HDFS
Create an input directory in HDFS, and copy the downloaded New York City Crime data file to HDFS:
cd $HADOOP_PREFIX
bin/hadoop fs -mkdir /hw1-input
bin/hadoop fs -put ~/NYPD_Complaint_Data_Current_YTD.csv /hw1-input/
Note: the environment variable $HADOOP_PREFIX can be activated by running the following command: source ~/.bashrc

# Program Execution
(a) Test python programs locally on master VM before running it in the Hadoop cluster.
cat NYPD_Complaint_Data_Current_YTD.csv | python hw1-mapper.py | sort | python hw1-reducer.py

(b) After uploading the crime data to HDFS, run program in Hadoop cluster as follows:
$HADOOP_PREFIX/bin/hadoop jar $HADOOP_PREFIX/contrib/streaming/hadoop-streaming-*.jar \
-input /hw1-input \
-output /hw1-output \
-file /home/cc/hw1-mapper.py \
-mapper /home/cc/hw1-mapper.py \
-file /home/cc/hw1-reducer.py \
-reducer /home/cc/hw1-reducer.py

# Troubleshooting Tips
(a) Hadoop does not allow you to run the same program with the same output directory more than once. To run the program multiple times, 
you need to either delete the previously used output directory, or use a new output directory.

(b) If a job is long-running, and you want to free the shell for other activities, you can let the job run in the
background by using: Ctrl-C

(c) If a job hangs (making no progress), you can fetch the job id and kill the job as follows:
bin/hadoop job –list
bin/hadoop job –kill job_2014----

(d) To troubleshoot the task that took too long or failed, take the following steps:
- Check which tasks have failed on which worker nodes by using the following command
bin/hadoop job –history <output-directory>
- Check the corresponding “stderr” file under the directory,
/usr/local/hadoop-1.2.1/logs/userlogs
