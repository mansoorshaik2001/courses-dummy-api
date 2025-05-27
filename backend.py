from fastapi import FastAPI, Request
app = FastAPI()
@app.get("/")
def hello():
    return "Hello"
@app.get("/users")
def show_users():
    return [
        {
            "name":"joy",
            "age" : 34
        },
        {
            "anme":"ally",
            "age" : 25
        }
    ]