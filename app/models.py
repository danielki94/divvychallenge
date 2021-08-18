from app import db
from datetime import datetime as dt

class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime, default=dt.utcnow)
    stoptime = db.Column(db.DateTime, default=dt.utcnow)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String)
    usertype = db.Column(db.String)
    trip_duration = db.Column(db.Integer)


    def __repr__(self):
        return f'<Trip: {self.trip_id}>'