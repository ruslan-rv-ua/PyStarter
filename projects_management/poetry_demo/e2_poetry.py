install 
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

poetry config virtualenvs.in-project true

poetry new md-converter

cd md-converter

poetry add markdown-it-pyrs

# .venv created

# .venv\scripts\activate
poetry shell

poetry add click

# poetry env info

poetry show

...

poetry build

# see dist folder

