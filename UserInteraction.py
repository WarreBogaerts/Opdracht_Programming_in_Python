import TaskManagerClass as TM
import pandas as pd

task_manager = TM.TaskManager()

start = input("Wat wil je doen? Voor help typ h. ")

if start.lower() == "h":
	print(
		'''
		Om een taak toe te voegen, reageer met a/A.
		Om een taak te starten, reageer met s/S.
		Om een taak te voltooien, reageer met c/C.
		Om een taak te verwijderen, reageer met d/D.
		Om alle taken te zien, reageer met t/T.
		Om een rapport naar .csv te exporteren, reageer met ec/EC.
		Om een rapport naar excel te exporteren, reageer met ex/EX.
		'''
		)

	start = input("Wat wil je doen? Voor help typ h. ")

	if start.lower() == "a":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")
		descr = input("Wat is de omschrijving voor de taak. ")

		#Add task
		task_manager.add_task(titel.title(),descr.title(),"INSERT INTO Tasks(Title, Description, Status_Id) VALUES(?,?, 1)")

	elif start.lower() == "s":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Start Task
		task_manager.start_task(titel.title(), "UPDATE Tasks set Status_Id = 2 Where Title LIKE ?")

	elif start.lower() == "c":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Complete task
		task_manager.complete_task(titel.title(), "UPDATE Tasks set Status_Id = 3 Where Title LIKE ?")

	elif start.lower() == "d":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Delete task
		task_manager.remove_task(titel.title())

	elif start.lower() == "t":
		#Show task
		rows = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		for row in rows:
			print(row)

	elif start.lower() == "ec":
		#.csv exporteren.
		data = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		df = pd.DataFrame(data)
		df.to_csv("tasks.csv", sep=",", index=False)

	elif start.lower() == "ex":
		#Excel exporteren
		data = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		df = pd.DataFrame(data)
		df.to_excel("tasks.xlsx", sheet_name="tasklist", index=False)




else:
	if start.lower() == "a":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")
		descr = input("Wat is de omschrijving voor de taak. ")

		#Add task
		task_manager.add_task(titel.title(),descr.title(),"INSERT INTO Tasks(Title, Description, Status_Id) VALUES(?,?, 1)")

	elif start.lower() == "s":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Start Task
		task_manager.start_task(titel.title(), "UPDATE Tasks set Status_Id = 2 Where Title LIKE ?")

	elif start.lower() == "c":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Complete task
		task_manager.complete_task(titel.title(), "UPDATE Tasks set Status_Id = 3 Where Title LIKE ?")

	elif start.lower() == "d":
		print("Geef volgende zaken door. ")
		titel = input("Wat is de titel van de taak. ")

		#Delete task
		task_manager.remove_task(titel.title())

	elif start.lower() == "t":
		#Show task
		rows = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		for row in rows:
			print(row)

	elif start.lower() == "ec":
		#.csv exporteren.
		data = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		df = pd.DataFrame(data)
		df.to_csv("tasks.csv", sep=",", index=False)

	elif start.lower() == "ex":
		#Excel exporteren
		data = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")
		df = pd.DataFrame(data)
		df.to_excel("tasks.xlsx", sheet_name="tasklist", index=False)

	else:
		print("U geeft de verkeerde letter in. Geef a,s,c,d of t in om verder te kunnen. Voor help typ h. ")
		start = input("Wat wil je doen? Voor help typ h. ")




