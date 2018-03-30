GET tasks:                   curl http://127.0.0.1:5000/tasks -X GET

POST task:                  curl http://127.0.0.1:5000/tasks -d "title=New task" -X GET

GET task(task_id):    curl http://127.0.0.1:5000/tasks/2 -X GET

PUT task(task_id):    curl http://127.0.0.1:5000/tasks/3 -d "title=New new task" -X PUT
