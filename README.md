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

### Using load_data_commands to load the data from data generation to tpcds database.

https://github.com/mmareddy943/singlestore/blob/main/load_data_commands

### Using optimize and analyze command scripts to optimize the tables.

https://github.com/mmareddy943/singlestore/blob/main/Optimize

### Using below script to execute 99-Queries 

https://github.com/mmareddy943/singlestore/blob/main/tpcds_99_queries









