#!/usr/bin/python3

"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests


if __name__ == "__main__":
    """
    this the unimportable script that gets the data
    """
    # declaration of variables
    url = "https://jsonplaceholder.typicode.com"

    # fully variables  definition
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users")
    todosUrl = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    userData = userUrl.json()
    todosData = todosUrl.json()
    numberOfUsers = len(userData)

    jsonDict = {}
    for user in userData:
        username = user["username"]
        userTasks = []
        for task in todosData:
            if task["userId"] == user["id"]:
                taskDict = {}
                taskDict['username'] = username
                taskDict['task'] = task['title']
                taskDict['completed'] = task['completed']
                userTasks.append(taskDict)
            else:
                continue
        jsonDict[user['id']] = userTasks

    with open(f"todo_all_employees.json", "w") as f:
        json.dump(jsonDict, f)
