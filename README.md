# Library



## Run Locally

Clone the project by running the blew command or download

```bash
  git clone https://github.com/RahmankhanA/Library
```

Go to the project directory

```bash
  cd Library
```
Create Virtual Environment by using this command

```bash
  python -m venv Environment_name
```
Activate Virtual Environment by using this command

```bash
   Environment_name\Scripts\sctivate.bat
```
Install dependencies  Python must be installed 

```bash
  pip install -r requirments.txt
```

Start the server
    
On Windows
```bash
  py manage.py runserver
```
OR 

```bash
  python manage.py runserver
```
On Linux

```bash
  python3 manage.py runserver
```
    


After that you could see that this project will start running on the 

    localhost:8000
    
    
    
    
    
## API Reference

#### To get all the video content you can make GET request on the given endpoint

```http
  GET localhost:8000
```

#### To upload video content  you can make POST request on the given endpoint

```http
  POST localhost:8000/upload/
```

