## Task Manager ✨📝

Task Manager helps you keep track of - you guessed it - tasks!  

> This study project focuses on syncing databases with Web and setting up custom models to work with each other nicely.  
I mean, it's all just Django ORM!

<li> Use authorization for picky access
<li> Create tasks and assign them to members
<li> Add statuses and labels for easier distinction
<li> Filter tasks by their content
<br>
..And also experience that strong "study project" vibe, of course.

<br>

> [Fourth project](https://ru.hexlet.io/programs/python/projects/52) of [@Hexlet](https://ru.hexlet.io/)'s Python Course

### [✨ Check out Task Manager live! ✨](https://python-project-52-731n.onrender.com)

Built on **Python** using **Django** and Bootstrap with the help of various libs.  
Uses **SQLite** (dev) and **PostgreSQL** (prod).  
Localized to Russian.  

> All kinds of badges:
[![Actions Status](https://github.com/alienflakes/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alienflakes/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/8aeca0c83ea81e559deb/maintainability)](https://codeclimate.com/github/alienflakes/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8aeca0c83ea81e559deb/test_coverage)](https://codeclimate.com/github/alienflakes/python-project-52/test_coverage)

## Local installation:
### Requirements: Python ^3.10, pip, poetry
Optional: your preferred DB engine. Built-in SQLite works just as fine for demo.

1. **Download** or simply clone the rep

```shell
pip install --user git+https://github.com/alienflakes/python-project-52.git
```

2. **Create a .env file** in the root directory and add these variables:
```
DATABASE_URL='sqlite:////absolute/path/db.sqlite3' or your db's schema

SECRET_KEY='enter or generate a key'

DEBUG=True/False (optional, defaults to False)
```

3. **Build the project**:
```shell
make build
```

4. **Run your local server**:
```shell
make dev
```
### And you're all set! Follow the link in the terminal to use the app ✨