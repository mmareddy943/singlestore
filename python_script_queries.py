import pymysql
import sys
import os
import argparse
import json
import re
from time import time, gmtime, strftime, sleep
from datetime import datetime, timedelta

def get_mysql_connection(user,passwd,host,database,port=3306):
     """
     :param user: Username
     :param passwd:  Passwd
     :param host: Host Name
     :param database: Database
     :param port: Default 3306
     :return: Mysql Connecter
     """

     try:
          return pymysql.connect(user=user,passwd=passwd,host=host,port=3306,database=database)
     except:
          print("Connecting to mysql database failing: {0}".format(sys.exc_info()[1:2]))

def read_json(json_file):
    """read json file
    Args:
        json_file (str): json file
    Returns:
        dict: json data
    """
    try:
        with open(json_file, "r") as f:
            _json_dict = json.load(f)
            return _json_dict
    except:
         print("unable to read json file : {0} and the error:\n {1}".format(json_file,sys.exc_info()[1:2]))

def execute_queries():
     """
     Args:
     Return:
     """
     try:
          user = "root"
          passwd = "password*******"
          host = "localhost"
          database = "tpcds"
          json_file = "queries.json"
          connection = get_mysql_connection(user,passwd,host,database)
          #sql_dict =  read_json(json_file)
          mycursor = connection.cursor()
          start_time = time()
          data = open('sample.txt','r').read()
          for query in data.split('$'):
               query_number = query.split("?")[0].lstrip("\n")
               sql_statement = query.split("?")[1]
               start = time()
               mycursor.execute(sql_statement)
               end = time()
               diff = end - start
               print("Q{0}:{1}".format(query_number,round(diff,3)))

          end_time = time()
          diff = end_time - start_time
          print("Total execution time : {0}".format(diff))
     except:
          print("Something ---- happen : \n {0}".format(sys.exc_info()[1:2]))
""" Main
"""
if __name__ == '__main__':
     try:
          execute_queries()
     except:
          print("Something wrong happen : \n {0}".format(sys.exc_info()[1:2]))
