# SQL playground

## Setup
### Virtual environment
```bash
python3 -m venv myenv
# activate virtual environment
source myenv/bin/activate
# install dependencies
pip install -r requirements.txt
# deactivate virtual environment after you are done
deactivate
```

### Run db seed script
```bash
# run from project-root/data-whisperer-backend/
python setup/create_and_seed_db.py
```

## Running the server
```bash
# run from project-root/data-whisperer-backend/
python run.py
```

## Running tests
```bash
# run from project-root/data-whisperer-backend/
pytest
```

## Handy commands
```bash
pip freeze > requirements.txt
```