# Casting Agency Project 
the Casting Agency project is the final project in the FSND udacity class. This project take stock of all what we have learned through the course of this nanodegree. In this Capstone project, you'll be challenged to use all of the concepts and the skills taught in the courses to build an API from start to finish and host it.

## Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The  Executive Producer within the company and are creating a system to simplify and streamline the  process.
### Models:
•	Movies with attributes title and release date
•	Actors with attributes name, age and gender
### Endpoints:
•	GET /actors and /movies

•DELETE /actors/ and /movies/

•	POST /actors and /movies and

•	PATCH /actors/ and /movies/
### Roles:
#### -	Casting Assistant
   
       •	Can view actors and movies

#### -	Casting Director
   
        •	All permissions a Casting Assistant has and…
   
        •	Add or delete an actor from the database
   
        •	Modify actors or movies

#### -	Executive Producer
  
     •	All permissions a Casting Director has and…
   
     •	Add or delete a movie from the database
### Tests:

•	One test for success behavior of each endpoint

•	One test for error behavior of each endpoint

•	At least two tests of RBAC for each role
