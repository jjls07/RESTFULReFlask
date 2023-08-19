from datetime import datetime

from flask import request

from app.Models.Tasks import Tasks

from app import app, db

from . import ControllerObject

import sqlalchemy


def GettAllTasks():
    ret = ControllerObject()

    try:
        ret.payload = [tasks.as_dict() for tasks in Tasks.query]
    except (Exception):
        ret.mensaje = "No se pudo realizar la consulta."
        ret.status = 400
    
    return ret



def SaveTask(task):
    ret = ControllerObject()

    try:
        task = Tasks(
            title=task.get("title"),
            date=datetime.strptime(task.get("date"), '%Y/%m/%d'),
            reminder=task.get("reminder")
        )

        db.session.add(task)
        db.session.commit()

        app.logger.info("Task successfully created.")
        ret.mensaje = "Task Created"
        
    except (Exception) as err:
        print(err)
        ret.mensaje = "No se puede completar la solicitud."
        ret.status = 400
    
    return ret

def manage_tasks(data):
    ret = ControllerObject()

    try:
        if request.method == 'GET':
            task = Tasks.query.get(data)

            if task:
                ret.payload = [Tasks.as_dict(task)]
            else:
                ret.mensaje = "Can't find the task."
                ret.status = 404
            
        elif request.method == 'POST':
            task = Tasks.query.get(data)
            
            if task:
                task.title = request.json["title"]
                task.date = request.json["date"]
                task.reminder = request.json["reminder"]

                db.session.commit()
                ret.mensaje = "Task modified"
            
            else:
                task = Tasks(
                    title=request.json["title"],
                    date=request.json["date"],
                    reminder=request.json["reminder"],
                )

                db.session.add(task)
                db.session.commit()
                ret.mensaje = "Task created"
                
        elif request.method == 'DELETE':

            task = Tasks.query.get(data)

            if task:
                db.session.delete(task)
                db.session.commit()
                ret.mensaje = "Task deleted"
            
            else:
                ret.mensaje = "Couldn't find the task."
                ret.status = 404
    
    except (Exception) as err:
        ret.mensaje = "Request couldn't be completed."
        ret.status = 400
    
    return ret