from app import db
from datetime import datetime


class Tasks(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    reminder = db.Column(db.Boolean())
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now()
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
    
    def __init__(self, title, date, reminder):
        self.title = title
        self.date = date
        self.reminder = reminder

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "reminder": self.reminder,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }