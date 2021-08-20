
# Django, htmx, and Tailwind CSS


## Setup
  
1. Create and activate a virtual environment:

```sh

$ python3 -m venv venv && source venv/bin/activate

```
2. Install the Python dependencies:

```sh
(venv)$ pip install -r requirements.txt

```
  
3. Install the Node dependencies:

```sh
$ npm install tailwindcss postcss postcss-cli autoprefixer @fullhuman/postcss-purgecss

# you may need to install PostCSS globally as well

# npm install --global postcss postcss-cli

```

4 . Apply the migrations and run the Django development server:

```sh
(venv)$ python manage.py migrate

(venv)$ python manage.py runserver
```

5.  Test at [http://localhost:8000/](http://localhost:8000/)
