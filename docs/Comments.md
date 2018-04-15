# Comments
In this project we have developed a RESTful web service using Python and the Flask microframework, using Flask-RESTful, a Flask extension that simplifies the creation of APIs. A curated list of any libraries and frameworks used can be found on the [requirements](https://github.com/ohduran/microservice/blob/master/requirements.txt) file.

This project relies on a virtual environment, an isolated folder which contains all the necessary executables to use the packages that the project needs.

## Intro
The task of designing a web service or API that adheres to the REST guidelines implies identifying the resources that will be exposed and how they will be affected by the methods.

We have built a To-Do list app that will be used in a local environment. To run, activate the virtual environment and then run the app by doing:

```shell
source environment/bin/activate
export FLASK_APP=run.py
flask run
```

After the server initializes, it will wait for client connections. The output indicates that the server is running on localhost IP address.

Check out the tests_unittest.py and see that there is a quick and reliable proof that every element of the code works as intended. You can run this on a different Terminal by changing directory to the folder and then doing:

```shell
source environment/bin/activate
python tests_unittest.py
```

## Technical Details
### Endpoints

- __GET /tasks__: Get a JSON object of all tasks for the user.
- __POST /tasks__: Post a new task under the user's list of tasks.

- __GET /task/task_id__: Get a JSON object of a given task filtered by task_id
- __PUT /task/task_id__: Update a given task filtered by task_id.
- __DELETE /task/task_id__: Delete a given task filtered by task_id.

- __PUT /markasdone/task_id__: Mark a given task filtered by task_id as done.

### Authentication
A Basic HTTP Authentication has been implemented using the Flask-HTTPAuth extension. No user handling was required, thus a hardcoded user was implemented, with a basic string password.
