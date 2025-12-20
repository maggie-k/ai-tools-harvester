import sqlite3
import os
import pandas as pd
from sqlalchemy import create_engine

def init_db():
	base_dir= os.path.abspath(os.path.dirname(__file__))
	data_dir= os.path.join(base_dir, 'data')
	os.makedirs(data_dir, exist_ok=True)
	db_path= os.path.join(data_dir, 'tools.db')
	print(db_path)

	conn= sqlite3.connect(db_path)
	conn.execute("PRAGMA foreign_key= ON")
	c= conn.cursor()

	c.execute('''CREATE TABLE IF NOT EXISTS tools (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	category TEXT NOT NULL,
	description TEXT NOT NULL,
	website TEXT NOT NULL''')

	for tool in tools:
		cursor.execute("INSERT INTO tools (name, category, description, website) VALUES (?, ?, ?, ?)",
			(tool["name"], tool["category"], tool["description"], tool["website"]))

	conn.commit()
	conn.close()

def hello(day):
	if day in ('Sat', 'Sun'):
		print ('Hello Weekend')
	else:
		print('Hello World')
#hello('Sun')