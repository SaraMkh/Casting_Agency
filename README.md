# Casting Agency Project (the backend)

The main activity for the Casting Agency is to produce some movie, also, assign actors to these movie. the executive producer has the responsibility of creating a system to simplify and streamline the Agency process.

## Motivation 
the Casting Agency project is the final project in the FSND udacity class. This project take stock of all what we have learned through the course of this nanodegree. In this Capstone project, we have been challenged to use all of the concepts and the skills taught in the courses to build an API from start to finish and host it.

### Project Dependencies

#### Python 3.8

the following link contains instructions to install the latest version of python [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

To keeps the dependencies for each project separate and organaized, follow the instructions that can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

after building the virtual environment, install dependencies by naviging to the the directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

#### How to run the development server

$ export FLASK_APP=app
$ export FLASK_ENV=development # enables debug mode
$ flask run app.py


## API Reference

Backend_Base URL: http://127.0.0.1:8080/

### Endpoints:
-GET '/'
    return welcome message.

            {
            'message':' Welcome to The Casting Agency company '
            }
-GET '/movies'
    return all available movies.

             {
                 "movies": [
                     {
                         "date": "Fri, 16 Dec 1988 21:30:00 GMT",
                         "id": 1,
                         "title": "Rain Man"
                     },
                     {
                         "date": "Fri, 20 Jun 2003 21:30:00 GMT",
                         "id": 2,
                         "title": "Hulk"
                     },
                     {
                         "date": "Fri, 08 Jan 2016 09:30:00 GMT",
                         "id": 3,
                         "title": "The Forest"
                     }
                 ],
                 "success": true
             }


-GET '/actors'
    return all available actors,

            {
                "actors": [
                    {
                        "age": 58,
                        "gender": "Male",
                        "movie_id": 1,
                        "name": "Thomas Cruise Mapother"
                    },
                    {
                        "age": 55,
                        "gender": "Female",
                        "movie_id": 1,
                        "name": "Valeria Golino"
                    },
                    {
                        "age": 53,
                        "gender": "Male",
                        "movie_id": 2,
                        "name": "Eric Banadinović "
                    },
                    {
                        "age": 38,
                        "gender": "Female",
                        "movie_id": 3,
                        "name": "Natalie Dormer"
                    },
                    {
                        "age": 37,
                        "gender": "Male",
                        "movie_id": 3,
                        "name": "Eoin Christopher Macken"
                    }
                ],
                "success": true
            }

-POST '/movies'
    Create a new movie,
    which will require the title and released date of the movie ,
        
            {
            "movie": (the entered movie)", 
            "success": true
            }

-POST '/actors'
    Create a new actor,
    which will require the name, age, gender and movie id (which movie he will acto in it) of the actor.
        
            {
            "actor": (the entered actor)", 
            "success": true
            }

-PATCH '/movies/<id>'
    Update an existing movie,
    which will require the title and released date of the movie.
        
            {
            "movie": (the movie after the Update)", 
            "success": true
            }
-PATCH '/actors/<id>'
    Update an existing actor,
    which will require the name, age, gender and movie id (which movie he will acto in it) of the actor.
        
            {
            "movie": (the actor after the Update)", 
            "success": true
            }
-DELETE '/movies/<id>'
    DELETE a movie using it's ID
    
            {
            "movie": (the movie after the Update)", 
            "success": true
            }
   -DELETE '/actors/<id>'
        DELETE a actor using it's ID

            {
            "movie": (the actor after the Update)", 
            "success": true
            }
#### How to run the test file 


To run the tests, run
```
$ dropdb Casting_AgencyTest
$ createdb Casting_AgencyTest
$ python3 test_app.py
```

## author
Sarah Mohammed and The udacity team that made the starter code of the Casting Agency Project .
