from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Form Page</title>
</head>
<body>
  <h1>Enter your name and phone number:</h1>
  <form action="submit_page" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required><br><br>
    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" required><br><br>
    <button type="submit">Submit</button>
  </form>
</body>
</html>
"""


@app.post("/submit_page", response_class=HTMLResponse)
def get_data(name: Annotated[str, Form()], phone: Annotated[str, Form()]):
    return f"""
<div>
    name: {name}
    <br>
    phone: {phone}
</div>
"""
