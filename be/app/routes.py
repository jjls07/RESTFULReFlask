from app import app
from flask import make_response


from flask import jsonify, request, Response, render_template

from app.Controllers import (
    TaskController as tasks,

)

@app.route("/tasks", methods=["GET"])
def GetAllTasks():
    result = tasks.GettAllTasks()
    return result.jsonify()


@app.route("/tasks", methods=["POST"])
def InsertTask():
    result = tasks.SaveTask(request.json)
    return result.jsonify()


@app.route("/tasks/<tid>", methods=["GET", "POST", "DELETE"])
def TasksTodos(tid):
    result = tasks.manage_tasks(tid)
    return result.jsonify()