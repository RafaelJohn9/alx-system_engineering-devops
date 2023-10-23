#!/usr/bin/python3

"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    """
    this the unimportable script that gets the data
    """
    # declaration of variables
    usrId = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    userTasks = []

    # fully variables  definition
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(usrId))
    todosUrl = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    userData = userUrl.json()
    todosData = todosUrl.json()

    username = userData["username"]
    for task in todosData:
        if task["userId"] == usrId:
            taskDict = {}
            taskDict['task'] = task['title']
            taskDict['completed'] = task['completed']
            taskDict['username'] = username
            userTasks.append(taskDict)
        else:
            continue
    user = {}
    user[str(usrId)] = userTasks

    with open(f"{usrId}.json", "w") as f:
        json.dump(user, f)
