# Langchain SQL Agent Bootstap

![Example 1](images/whisp_10.PNG)
![Exampe 2](images/whisp_11.PNG)
## TODOs
- [ ] add file upload to the UI (currently you can seed the db with `data-whisperer-backend/setup/create_and_seed_db.py`)
- [ ] autorefresh for the tables after commands have been run
- [ ] cleanup the langchain text on the next execute instead of appending to it

## Running locally

Use Python 3.10.10

### Backend
Create virtual environment (only need to do this once)
```bash
python3 -m venv data-whisperer-backend/myenv
```
activate virtual environment
```bash
source data-whisperer-backend/myenv/bin/activate
# install dependencies
pip install -r data-whisperer-backend/requirements.txt
# create and seed db
python data-whisperer-backend/setup/create_and_seed_db.py
```

run the backend
```bash
python data-whisperer-backend/run.py
```

### Frontend
```bash
cd data-whisperer-ui/
npm install # only need to do this once
npm start
```

## Teardown
```bash
# deactivate virtual environment after you are done
deactivate
```
