# DBC - CSV Converter and Pusher
## Set up
### 1. Install libraries ```os```, ```subprocess``` and ```sys``` (all of them should be among global libraries)
### 2. In terminal, cd to directory converter
### 3. In run.py change your web adress to your git repository with all dbcs (line no. 4)
### 4. Initialize commands:
```python run.py update``` -> ```python run.py csv```
## Usage:
### Convert dbc to csv for inDB usage:
```python run.py csv```
### Convert csv to dbc (csvs should be changed by the DB):
#### If no push to repo is needed:
```python run.py dbc```
#### If push is also needed:
```python run.py```

### Also works for individual files by typing their names (f.e. Item or Holidays) as next argument:
```python run.py dbc item```
