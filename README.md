# ConnectART

Connectart is a social media web application designed to connect CESAR School's students through their taste in art, such as movies, books, music and TV shows.

With the COVID 19 pandemics, students were forced to migrate to online classes. As well as moving away from the physical teaching environment, they also moved away from social interaction. 
ConnectART grew out of a need for students to connect with each other, matching their common interests.

### Developers:
- Lorena Seabra
- Luís Cruz
- Marcela Azoubel
- Mateus Rebêlo
- Rodrigo Cavalcanti

### Product Owner:
- Ricardo Costa 

### Software Engineering concepts used in this project
- Software Requirements (User stories, Storyboards)
- Agile development (Scrum, CI/CD, Pair Programming)
- Software Design (Software Modeling, Class Diagrams, UML)
- GRASP
- Test Driven Development
- DevOps (Software versioning systems, Continuous Integration, Continuous Deployment)
- Refactoring

### Integration/Deployment Workflow
- Write code
- Commit changes
- Run tests locally
- Push to remote repo
- CI automatically runs tests
- If CI is successfull, CD tool automatically deploys to Heroku

### Installing the project on your machine
The entirety of this project is developed using Python with its Django framework for web development. In order to avoid conflicting dependencies with other Python projects in your machine, it's a good ideia to activate a Python Virtual Environment (venv). The project is standardized to use Python 3.9.12, but if you have at least 3.9, it should be no problem.
The following step should be taken within the root directory of the project once you ``git clone`` it into your machine.

To activate a venv on Linux:<br>
``python3 -m venv venv``<br>
Then run the script located at<br>
``./venv/bin/activate``<br>

To activate a venv on Windows (preferrably using PowerShell) <br>
``py -m venv venv``<br>
Then run the script located at<br>
``.\venv\Scripts\Activate.ps1``<br>

Once it is activated, you can type:<br>
``pip install -r requirements.txt``<br>
so pip can install every required package for the project.<br>

And finally, if all goes well, you can run the project by typing:<br>
Linux:<br>
``python3 manage.py runserver``<br>

Windows:<br>
``py manage.py runserver``<br>

And that's it. Any doubts about the structure and functioning of a Django project can be answered on their [Wiki](https://docs.djangoproject.com/en/4.0/).