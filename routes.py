from flask import render_template, request, redirect, url_for
from . import db
from .models import Match, Prediction
import requests
from datetime import datetime

def get_matches():
    response = requests.get('https://api.football-data.org/v2/competitions/EC/matches', headers={'X-Auth-Token': 'YOUR_API_KEY'})
    data = response.json()
    matches = []
    for match in data['matches']:
        matches.append(Match(
            id=match['id'],
            home_team=match['homeTeam']['name'],
            away_team=match['awayTeam']['name'],
            match_date=datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
        ))
    return matches

@routes.route('/')
def index():
    matches = get_matches()
    return render_template('index.html', matches=matches)

@routes.route('/submit_prediction', methods=['POST'])
def submit_prediction():
    match_id = request.form['match_id']
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    user = request.form['user']

    prediction = Prediction(user=user, match_id=match_id, home_score=home_score, away_score=away_score)
    db.session.add(prediction)
    db.session.commit()

    return redirect(url_for('index'))
