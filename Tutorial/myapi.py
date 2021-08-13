from fastapi import FastAPI

app = FastAPI()

#localhost/delete-user
#amazon.com/create-user =endpoint is creating a new user 
#GET- get or return an information
#POST- create something new
#PUT- update data
#DELETE- delete something

@app.get("/")
def index():
    return {"name": "First Data"}