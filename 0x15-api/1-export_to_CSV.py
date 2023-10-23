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
    noOfTasks = 0
    tasksDone = 0
    titlesOfTasks = []

    # fully variables  definition
    userUrl = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(usrId))
    todosUrl = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    userData = userUrl.json()
    todosData = todosUrl.json()

    username = userData["name"]
    for task in todosData:
        if task["userId"] == usrId:
            titlesOfTasks.append(task["title"])
            noOfTasks += 1
            if task["completed"]:
                titlesOfTasks.append(task["title"])
                tasksDone += 1
        else:
            continue

    # output
    with open("./USER_ID.csv", "w") as f:
        for title in titlesOfTasks:
            f.write('"{}", "{}", "{}", "{}"\n'
                    .format(usrId, username, task['completed'], title))
