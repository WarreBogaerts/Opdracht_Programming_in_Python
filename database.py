import sqlite3

def connectie():
	return sqlite3.connect("TaskManager.db")

