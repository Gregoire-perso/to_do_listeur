#!/bin/python3
# Task manager
# See readme.md to have more informations

# Global import
import mysql.connector;

# Local import
import connections;
import task_managment;
import errors;

# Connection to mysql db
mydb = mysql.connector.connect(
        host="localhost", 
        user="task_manager", 
        password="task_manager", 
        database="Task_manager");
cursor = mydb.cursor();

status = "connection"
while(status == "connection"):
    try:
        user = connections.connection(cursor);

    except errors.WrongConnection:
        print("Les identifiants sont incorrectes...");
        new_account = input("Voulez-vous créer un nouveau compte ? ");
        if(new_account.lower() in "ouiyes"):
            user = connections.new_account(cursor);
            print("Création de votre compte réussie !");
            status = "menu";

    else:
        print("Connexion réussie");
        status = "menu";


while(status == "menu"):
    print("Que voulez vous faire ?\n", \
            "1 : Afficher toutes vos tâches en cours\n", \
            "2 : Ajouter une nouvelle tâche\n", \
            "3 : Quitter");
    choice = int(input());

    if(choice == 1):
        task_managment.show_all(cursor, user);

    elif(choice == 2):
        task_managment.add_task(cursor, user);

    elif(choice == 3):
        print("Au revoir !")
        cursor.close();
        mydb.close();
        quit();


