from main import db
from flask_sqlalchemy import SQLAlchemy

class Entry(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.Text)
   address = db.Column(db.Text)
   need = db.Column(db.Text)
   
   def __repr__(self):
       return "<Entry id={} name={!r} address={!r} need={!r}>".format(self.id, self.name, self.address, self.need)

def init():
   db.create_all()