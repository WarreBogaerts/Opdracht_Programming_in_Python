import database as db
import TaskManagerClass as TM

task_manager = TM.TaskManager()

taak = "Taak 4"
descr = "Dit is een test"
status = 1

#Add task
task_manager.add_task('Taak 4',"INSERT INTO Tasks(Title, Description, Status_Id) VALUES('Taak 4','Dit is een test', 1)")

#Start Task
task_manager.start_task('Taak 4', "UPDATE Tasks set Status_Id = 2 Where Title LIKE ?")

#Complete task
task_manager.complete_task('Taak 4', "UPDATE Tasks set Status_Id = 3 Where Title LIKE ?")

#delete task
task_manager.remove_task('Taak 4')

#Show task
rows = task_manager.display_tasks("SELECT Title, Description, Name FROM Tasks JOIN Status on Tasks.Status_Id = Status.Status_Id")



for row in rows:
	print(row)
