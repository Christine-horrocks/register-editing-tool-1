from application.extensions import db
from datetime import datetime
from random import randint

def random_integer():
    min_ = 100
    max_ = 1000000000
    rand = randint(min_, max_)

    return rand

class DynamicModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, default=random_integer, unique=True, nullable=False)
    # uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    schema = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(15), nullable=False, default='draft')
    json_blob = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"DynamicModel('{self.id}', '{self.uuid}', '{self.schema}', '{self.status}', '{self.json_blob}')"


