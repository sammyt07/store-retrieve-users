# Pseudocode by Sammy:
# prompt user for their name and age
# store user in SQLite by name and age
# retrieve users by name

# main
# create a new user
# store user in database
# retrieve user from database

# promptName - prompt user for name
# promptAge - prompt a user for their age
# storeUser - store user's name and age in SQLite
# getUser - get a user by their name from SQLite

# Code solution by Sammy,
# references: https://docs.python.org/3/library/sqlite3.html,
#             https://www.sqlitetutorial.net/sqlite-update/
#             https://docs.python.org/3/tutorial/classes.html
#             https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
import sqlite3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def promptName():
    """
        Prompt the user to enter their name in O(n).
        Output: name - a string representing the user's name.
    """
    name = input("Enter your name: ")

    # validate name is only characters
    for i in range(len(name)):
        if (name[i].isalpha() == False):
            print("Error: enter only alphebatical characters.\n")
            name = input("Enter your name: ")

    return name

def promptAge():
    """
        Prompt the user to enter their age in O(n).
        Output: age - a string repesenting the user's age.
    """
    age = input("Enter your age: ")

    # validate age is numeric
    for i in range(len(age)):
        if (age[i] in "0123456789") == False:
            print("Error: enter only numerical digits.\n")
            age = input("Enter your age: ")

    return age

def storeUser(con, cur, user):
    """
        Stores the user in a database in O(1).
        Inputs: con - connection object to the database.
                cur - database cursor object.
                user - the Person object being stored.
    """
    cur.execute(f"INSERT INTO user VALUES ('{user.name}', {user.age})")
    con.commit()

def getUser(cur, name):
    """
        Given a user's name, retrieve their information in O(1).
        Inputs: cur - database cursor object,
                name - string representation of the user's name.
    """
    cur.execute(f"SELECT name, age FROM user WHERE name='{name}'")
    
    res = cur.fetchone()
    if res is None:
        print(f"Error: there is no row with the name '{name}'")
    return res

def removeUser(con, cur, name):
    """
        Given a user's name, remove their information in O(1).
        Inputs: cur - database cursor object,
                name - string representation of the user's name.
    """
    cur.execute(f"SELECT name, age FROM user WHERE name='{name}'")
    res = cur.fetchone()
    if res is None:
        print(f"Error: there is no row with the name '{name}'")
    else:
        cur.execute(f"DELETE FROM user WHERE name='{name}'")
        con.commit()

def getAllUsers(cur):
    """
        Prints all users' names and ages in O(1).
        Input: cur - database cursor object.
    """
    cur.execute("SELECT * FROM user")
    res = cur.fetchall()
    print(res)

def modifyUser(con, cur, user, newUser):
    """
        Modify's the given user's name and age in O(1).
        Inputs: con - connection to the database.
                cur - database cursor object.
                user - string representation of the user's name.
                newUser - Person object for the new user.
    """
    db_entry = cur.execute(f"SELECT name, age FROM user WHERE name='{user}'")
    cur.execute(f"UPDATE user SET name='{newUser.name}', age='{newUser.age}'")
    con.commit()

def main():
    con = sqlite3.connect("user-info.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(name, age)")

    # User choices:
    # 1 - store a new user
    # 2 - edit a user
    # 3 - remove a user
    print("----------User Choices----------")
    print("1) Store a new user")
    print("2) Get an existing user")
    print("3) Remove an existing user")
    print("4) Edit an existing user")
    userChoice = input("Choose: ")

    # ------ Handle Input ------
    match userChoice:
        case '1':
            name = promptName()
            age = promptAge()
            newUser = Person(name, age)
            storeUser(con, cur, newUser)
        case '2':
            name = promptName()
            print(getUser(cur, name))
        case '3':
            name = promptName()
            removeUser(con, cur, name)
        case '4':
            print("Which user would you like to edit?")
            getAllUsers(cur)
            user = input("Enter a name: ")  # lookup user by name
            newName = input("Enter a new name: ")
            newAge = input("Enter a new age: ")
            newUser = Person(newName, newAge)
            modifyUser(con, cur, user, newUser)

if __name__ == "__main__":
    main()
