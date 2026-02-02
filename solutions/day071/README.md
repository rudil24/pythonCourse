# Going to Production: Notes
Here are things to consider when taking a Python application to a "live" web production environment:
1. always use version control (git AND Github, because most providers link to your Github for source code AND they usually have auto-refresh when you change and push main to Github)
2. use a .gitignore in your local project root folder, preferrably one that's [built for Python](https://github.com/github/gitignore/blob/main/Python.gitignore) 
   * make SURE .env is ignored in your .gitignore
3. store keys & private info in your local .env (should back that up somewhere local too, since Github won't), then `import os` library in whatever .py's these vars are found, replace keys with `os.environ.get("KEY_NAME")` to recall them at runtime
   * ex: app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
4. enable a WSGI (Web Server Gateway Interface) in your requirements.txt. The most popular of these is [gunicorn](https://gunicorn.org/). 
5. create Procfile in project root directory (named exactly `Procfile`, no dot extension, that summons the WSGI for your app.) 
   * if using gunicorn, and your app is in main.py, your Procfile looks like:
   * `web: gunicorn main:app` 
6. commit the above production changes and **push to Github**
7. sign up (or use your existing account) for one of the Python-ready providers:
   1. [Render](https://render.com/pricing)
   2. [PythonAnywhere](https://www.pythonanywhere.com/)
   3. [Cyclic](https://www.cyclic.sh/pricing/)
   4. [Vercel](https://vercel.com/pricing)
   5. [Heroku](https://www.heroku.com/pricing) **no longer has a free tier**
   6. [article about these and others](https://www.python-engineer.com/posts/hosting-platforms-for-python/)
8. Create a new "web service" with your provider (or whatever the provider's language for that. Before hitting the final "create web service" or "deploy"): 
   1. link your Github repo to the provider (see provider docs, they all have a way to do it)
   2. edit the start command to be what's in your Procfile  *rl note: why can't they just read our Procfile?*
   3. set your environment variables, see provider docs on how to do it
      * remember, your linked Github repo won't have them, b/c you properly gitignored publishing them, they should only exist in your local .env file
   4.  CRUD-ing (need data?) with this app? 
       * spin up a PostGres database with the provider (you usually only get one on free plan, so consider naming it generic "username_db" and looking up how to use partitions for multiple portfolio projects)
   5.  link the PostGres database to your web service
       * Set your SQLALCHEMY_DATABASE_URI environment variable
       * paste the provider's db address it into your environment variable, but if it starts with postgres:// change it to __postgresql://__  (required for SQLAlchemy)
       * *WAIT! didn't we build our app with an SQLite db?* __That's OK:__ The reason we can seamlessly switch from SQLite to Postgres is because we are using the psycopg package in combination with SQLAlchemy. 
