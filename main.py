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
# references: https://docs.python.org/3/library/sqlite3.html
import sqlite3

def promptName():
    """
        Prompt the user to enter their name.
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
        Prompt the user to enter their age.
        Output: age - a string repesenting the user's age.
    """
    age = input("Enter your age: ")

    # validate age is numeric
    for i in range(len(age)):
        if (age[i] in "0123456789") == False:
            print("Error: enter only numerical digits.\n")
            age = input("Enter your age: ")

    return age

def storeUser(con, cur, name, age):
    """
        Stores the user in a database.
        Inputs: con - connection object to the database.
                cur - database cursor object.
                name - string representation of the user's name.
                age - string representation of the user's age.
    """
    cur.execute(f"INSERT INTO user VALUES ('{name}', {age})")
    con.commit()

def getUser(cur):
    """
        Given a user's name, retrieve their information.
        Input: cur - database cursor object.
    """
    name = input("Enter a user's name: ")

    # validate name is alphebatical
    for i in range(len(name)):
        if name[i].lower().isalpha() == False:
            print("Error: enter only alphabetical characters.")
            name = input("Enter a user's name")

    cur.execute(f"SELECT name, age FROM user WHERE name='{name}'")
    
    res = cur.fetchone()
    if res is None:
        print(f"Error: there is no row with the name '{name}'")
    else:
        print(res)

def main():
    name = promptName()  # get name in O(n)
    age = promptAge()  # get age in O(n)

    con = sqlite3.connect("user-info.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(name, age)")

    storeUser(con, cur, name, age)  # store user in O(1)
    print(getUser(cur))  # lookup in O(1)

if __name__ == "__main__":
    main()
