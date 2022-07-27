## Setup

### Linux

Make sure the required development tools are installed:

CentOS/RHEL:
```
yum install gcc make flex bison byacc git
```

Run the following commands to clone the repo and build the tools:

git clone https://github.com/gregrahn/tpcds-kit.git

cd tpcds-kit/tools

make OS=LINUX

### Create directory for Flat files (for SF=1000, need 1024 GB Space)

create directory for flat files uisng below command..if you dont have space locally..create external volume and attach to the VM

mkdir /tpdds

in my test methodolgy, i have created external space and mounted to /tpdds.for this we need below steps to mount the volume.

parted /dev/sdb mklabel gpt

parted /dev/sdb mkpart primary 2048s 100%

partprobe /dev/sdb

mkfs.xfs /dev/sdb1

mkdir -p /tpdds

mount -a

### Using dsdgen to generate the data
Data generation is done via dsdgen. See dsdgen -help for all options. 

cd /root/tpcds-kit/tools

execute the below command to generate the data

./dsdgen -sc 1000 -f -DIR /tpdds/

it has generated total 24 files with total 917 GB.

### Using Create Tables in column store file to create tpcds database and create tables below is the files link

https://github.com/mmareddy943/singlestore/blob/main/Craete%20Tables%20in%20ColumnStore

### Using Below script to load the data from data generation to tpcds database.

#!/bin/bash

#Created by Mahesh Anand Reddy

start=$(date +%s.%N)

touch file_log.log

for f_name in `ls /tpcds/*.dat`;

do

t_file=$(echo "${f_name##*/}")

t_name=$(echo "${t_file%.*}")

load_tpcds_data="LOAD DATA LOCAL INFILE '$f_name' INTO TABLE $t_name FIELDS TERMINATED BY '|' LINES TERMINATED BY '|\n';"

memsql -u root -p -h ****** --local-infile=1 -D tpcds -e "$load_tpcds_data" >> file_log.log

done

duration=$(echo "$(date +%s.%N) - $start" | bc)

execution_time=`printf "%.2f seconds" $duration`

echo "Script Execution Time: $execution_time"

NOTE: Before executing the script,add hostname in memsql statement instead of ****.

###Using optimize and analyze command scripts to optimize the tables.

https://github.com/mmareddy943/singlestore/blob/main/Optimize

###Using below script to execute 99-Queries 
I have created python script to autocapture the query timings for the 99-queries. The script has uploaded in the below link.

https://github.com/mmareddy943/singlestore/blob/main/python_script_queries.py

NOTE: sample.txt file also uploaded in the below link. 

https://github.com/mmareddy943/singlestore/blob/main/sample.txt

----------------------------------------------------
Sample Output:
[root@pyth-vm ~]# python3 test.py

Q1:12.524
Q2:48.08
Q3:0.512
Q4:282.88
Q5:35.325
Q6:25.614
Q7:9.072
Q8:2.281
Q9:13.205
Q10:8.629
Q11:127.664
Q12:0.707
Q13:4.421
Q14:133.187
Q15:3.654
Q16:38.113
Q17:6.818
Q18:9.521
Q19:1.26
Q20:0.734
Q21:0.634
Q22:1.09

-------------------------------------------------------------------

**References:**
https://github.com/gregrahn

https://www.singlestore.com/blog/tpcds-benchmarking-showdown-a-singlestore-pov/






