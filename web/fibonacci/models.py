from fibonacci import db
import datetime


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, url):
        self.url = url
