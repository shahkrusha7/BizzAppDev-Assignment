"""
Task Scheduling Problem 

Problem:
Given a list of tasks, each with a deadline and duration,
find the maximum number of tasks that can be completed without missing their deadlines.

Approach:
1. Sort tasks by deadline.
2. Add tasks one by one if they can be completed before their deadline.
3. Return the total number of tasks that fit.
"""

def schedule_tasks(tasks):
    tasks.sort(key=lambda t: t['deadline'])
    time=0
    count=0
    for task in tasks:
        if time+task['duration']<=task['deadline']:
            time+=task['duration']
            count+=1
    return count

tasks=[
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

print("Maximum number of tasks:", schedule_tasks(tasks))
