# Data whisperer

## Running locally
### Backend
```bash
# create virtual environment (only need to do this once)
python3 -m venv data-whisperer-backend/myenv
# activate virtual environment
source data-whisperer-backend/myenv/bin/activate
# install dependencies
pip install -r data-whisperer-backend/requirements.txt
# run script
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
