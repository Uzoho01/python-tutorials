# database
# data types in sqlite3

from msilib import Table
import sqlite3 
var = sqlite3.connect("indiv.db")
c = var.cursor()
# creating tables
c .execute("CREATE TABLE users ")

var.close()
