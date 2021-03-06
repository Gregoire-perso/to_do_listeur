# File for displays functions
# Global import
import time;

def show_all(cursor, user):
    """mysql.connector.cursor_cext, tuple -> None
    Display all task of the account """
    cursor.execute("SELECT * FROM Task WHERE user='{0}';".format(user[0]));
    task = cursor.fetchone();
    
    while(task):
        print("Date de création : {1}\nDate limite : {2}\nEtat : {3}\nPriorité : {4}\nDescription : {6}".format(task));
        task = cursor.fetchone();

#----------------------------------------------------------------------------------------

def add_task(cursor, user):
    """mysql.connector.cursor_cext, tuple -> None
    Add a task in mysql db """
    description = input("Entrez le descriptif de la tâche : ");
    deadline = input("Entrez une date limite (format AAAA/MM/JJ) ou rien sinon : ");
    deadline = deadline.replace("/", "");
    if(deadline == ''):
        deadline = 0;

    priority = int(input("Entrez un ordre de priorité (de 1 à 10) : "));
    cursor.execute("INSERT INTO Task (creation_date, deadline, state, priority, user, description) VALUES({0}, {1}, {2}, {3}, '{4}', '{5}');".format(time.strftime("%Y%m%d"), deadline, 2, priority, user[0], description));
