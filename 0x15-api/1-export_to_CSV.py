#!/usr/bin/python3

"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    """
    this the unimportable script that gets the data
    """
    # declaration of variables
    usrId = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    # fully variables  definition
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(usrId))
    todosUrl = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    userData = userUrl.json()
    todosData = todosUrl.json()

    username = userData["name"]

    # output
    with open(f"./{usrId}.csv", "w") as f:
        for task in todosData:
            if task['userId'] == usrId:
                f.write('"{}", "{}", "{}", "{}"\n'
                        .format(usrId,
                                username,
                                task['completed'],
                                task['title']))
