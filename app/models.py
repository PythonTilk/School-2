from . import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(50))
    away_team = db.Column(db.String(50))
    match_date = db.Column(db.DateTime)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
