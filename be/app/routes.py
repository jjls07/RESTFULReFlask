from app import app
from flask import make_response


from flask import jsonify, request, Response, render_template
import requests

from app.Controllers import (
    TaskController as tasks,

)

@app.route("/tasks", methods=["GET"])
def GetAllTasks():
    result = tasks.GettAllTasks()
    return result.jsonify()