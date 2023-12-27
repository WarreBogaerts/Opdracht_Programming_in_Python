import database as db

dbConnectie = db.connectie()
cursor = dbConnectie.cursor()

class TaskManager:

    def add_task(self,task_name, query):
        test_query = "SELECT Title FROM Tasks"
        cursor.execute(test_query)
        rows = cursor.fetchall()

        add_query = query
        cursor.execute(add_query)
        dbConnectie.commit()

        print("De taak is aangemaakt. Nu kan u deze starten, afwerken of verwijderen.")
        


    def start_task(self, task_name, query):
        test_query = "SELECT Title FROM Tasks"
        cursor.execute(test_query)
        rows = cursor.fetchall()

        if rows.index((task_name,)) != None:
            update_query = query
            parameter = (task_name,)

            cursor.execute(update_query, parameter)
            dbConnectie.commit()
            
            cursor.execute(test_query)
            check = cursor.fetchall()

            if task_name in check:
                print("Het starten van de taak is niet gelukt. Probeer opnieuw.")
                
            else:
                print("De taak is gestart.")
                

        else:
            print("De taak bestaat niet. U moet de taak eerst aanmaken voor u hem kan starten.")

    def complete_task(self, task_name,query):
        test_query = "SELECT Title FROM Tasks"
        cursor.execute(test_query)
        rows = cursor.fetchall()

        if rows.index((task_name,)) != None:
            update_query = query
            parameter = (task_name,)

            cursor.execute(update_query, parameter)
            dbConnectie.commit()
            
            cursor.execute(test_query)
            check = cursor.fetchall()

            if task_name in check:
                print("Het afwerken van de taak is niet gelukt. Probeer opnieuw.")
                
            else:
                print("De taak is afgewerkt.")
                

        else:
            print("De taak bestaat niet. U moet de taak eerst aanmaken voor u hem kan afwerken.")


    def remove_task(self, task_name):
        test_query = "SELECT Title FROM Tasks"
        cursor.execute(test_query)
        rows = cursor.fetchall()

        if rows.index((task_name,)) != None:
            delete_query = "DELETE FROM Tasks Where Title LIKE ?"
            parameter = (task_name,)

            cursor.execute(delete_query, parameter)
            dbConnectie.commit()
            
            cursor.execute(test_query)
            check = cursor.fetchall()

            if task_name in check:
                print("Het verwijderen van de taak is niet gelukt. Probeer opnieuw.")
                
            else:
                print("De taak is verwijderd.")
                

        else:
            print("De taak bestaat niet. U moet de taak eerst aanmaken voor u hem kan verwijderen.")
            
        
    def display_tasks(self, query):
        display_query = query
        cursor.execute(display_query)

        rows = cursor.fetchall()
        return rows