# SQL playground

## Setup
### Virtual environment
```bash
python3 -m venv myenv
# activate virtual environment
source myenv/bin/activate
# install dependencies
pip install -r requirements.txt
# run script
python main.py
# deactivate virtual environment after you are done
deactivate
```
### Install dependencies
```bash
pip install -r requirements.txt
```



### Database - fuck docker for now
```bash
docker pull keinos/sqlite3:latest
```

```bash
docker run --rm -it -v "$(pwd):/workspace" -w /workspace keinos/sqlite3
```

## Handy commands
```bash
pip freeze > requirements.txt
```