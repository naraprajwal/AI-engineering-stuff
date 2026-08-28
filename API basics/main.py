from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message : hello world"}

@app.get("/about")
def aboutme():
    return {"message : Prajwal Nara 3rd year btech student at iith"}
