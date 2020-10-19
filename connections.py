#!/bin/python3
# Programme permettant de gérer une todo list
# La gestion se fait via mysql
# Utilisateur  : todo_list
# Mot de passe : todo_list

# Global import
import getpass;

# Local import
import errors;

def connection(cursor, username="", passwd=""):
    """mysql.connector.cursor_cext -> String
    User identification that return username if connection is correctly done """
    if(len(username) == 0 and len(passwd) == 0):
        username = input("Entrez votre nom d'utilisateur : ");
        passwd = getpass.getpass("Entrez votre mot de passe : ");

    cursor.execute("SELECT username, name, surname FROM User WHERE username='{0}' AND passwd='{1}';".format(username, passwd));
    user = cursor.fetchall();
    
    if(len(user) == 0):
        raise(errors.WrongConnection);
    else:
        return(user[0]);

#----------------------------------------------------------------------------------------

def new_account(cursor):
    """mysql.connector.cursor_cext -> String
    Ask user informations to create a new account """
    username = input("Entrez l'identifiant que vous voulez utiliser (il ne sera pas modifiable plus tard) : ");
    surname = input("Entrez votre prénom : ");
    name = input("Entrez votre nom : ");
    passwd = input("Entrez votre mot de passe : ");
    
    cursor.execute("SELECT username FROM User WHERE username='{0}';".format(username));
    already_exists = cursor.fetchall();
    if(len(already_exists) != 0):
        print("Identifiant déjà utilisé...");
        return(new_account(cursor));

    else:
        cursor.execute("INSERT INTO User (username, name, surname, passwd) VALUES ('{0}', '{1}', '{2}', '{3}');".format(username, name, surname, passwd));
        return(connection(cursor, username=username, passwd=passwd));
