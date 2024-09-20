from flask import render_template, request
from .. import app


@app.get("/result")
def result():
    message = request.form.get("text")
    return render_template("result.html", message=message)