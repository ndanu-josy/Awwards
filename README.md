# Instagram

## Author
Josphine Ndanu

## Description
Awwards is a website where a user can register for an acccount, post projects as well as rate other people's projects. 

## Set Up and Installations

### Prerequisites
1. Python version 3.8
2. Django 
3. Pip
4. Virtual Environment(venv)


### Clone the  project 
Run the following command on the terminal:
`git clone https://github.com/ndanu-josy/Awwards.git`


###  Project Setup
1. Create virtual environment (python3 -m venv virtual)
2. Activate virtual environment (. virtual/bin/activate)
3. Install  all dependancies ( pip install -r requirements.txt)
4. Create database (CREATE DATABASE projawwrds;)
5. Make migrations

    #### Database Migrations
    python3 manage.py makemigrations awwardsapp
    python3 manage.py migrate

6. Run the application
    ### Run 
    python3.8 manage.py runserver

7.  Testing the application
     python3 manage.py test awwardsapp

### Admin Dashboard
    (https://theawwards.herokuapp.com/admin)
    username: moringa
    password: moringa123


### Acccessing the API 
[Profiles Endpoint](https://theawwards.herokuapp.com/api/profileApi)
[Projects Endpoint](https://theawwards.herokuapp.com/api/projectsApi)    

### Search functionality
    search by project name 

## Technologies used
    Python 3.8
    Bootstrap
    Django
   
## Live Sute

[View Live Site.](https://theawwards.herokuapp.com/)

## License

This project is under the [MIT](LICENSE) license.
