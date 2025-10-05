from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Tabella

import json

views = Blueprint('views', __name__)


@views.route('/')
def start():
    from flask_login import current_user
    return render_template('start.html', user=current_user)

# Route per la tabella
@views.route('/tabella')
@login_required
def tabella():
    from flask_login import current_user
    # Initialize data only if table is empty
    if not Tabella.query.first():
        cognomi = [
            'BANDINI', 'BARACTARI', 'BARDARO', 'BASILI', 'BATTAGLIA', 'BERGHENTI', 'BOI', 'BONORETTI',
            'CONTRERAS', 'FILIPPINI', 'FOGLIA', 'GIANINI', 'HUERTA', 'IOSUE', 'JABARI', 'LENA',
            'PASCARELLA', 'PIGHI', 'PINOTTI', 'SOLI', 'VETRO', 'ZIVERI'
        ]
        for i, cog in enumerate(cognomi, 1):
            new_row = Tabella(
                cognome=cog,
                checked=True,
                punti=0,
                probabilita=100 - i*2
            )
            db.session.add(new_row)
        db.session.commit()
    tabella_data = Tabella.query.all()
    names = [row.cognome for row in tabella_data]
    return render_template('tabella.html', tabella_data=tabella_data, names=names, user=current_user)

@views.route('/save_tabella', methods=['POST'])
@login_required
def save_tabella():
    data = request.get_json()
    for row in data:
        tab = Tabella.query.get(row['id'])
        if tab:
            tab.checked = row['checked']
            tab.punti = int(row['punti'])
            tab.probabilita = float(row['probabilita'])
            tab.stato = row['stato']
    db.session.commit()
    return jsonify({'success': True})

@views.route('/reset_data', methods=['POST'])
@login_required
def reset_data():
    # Reset all Tabella rows to default values
    cognomi = [
        'BANDINI', 'BARACTARI', 'BARDARO', 'BASILI', 'BATTAGLIA', 'BERGHENTI', 'BOI', 'BONORETTI',
        'CONTRERAS', 'FILIPPINI', 'FOGLIA', 'GIANINI', 'HUERTA', 'IOSUE', 'JABARI', 'LENA',
        'PASCARELLA', 'PIGHI', 'PINOTTI', 'SOLI', 'VETRO', 'ZIVERI'
    ]
    # Delete all existing rows
    Tabella.query.delete()
    # Reinitialize with default data
    for i, cog in enumerate(cognomi, 1):
        new_row = Tabella(
            cognome=cog,
            checked=True,
            punti=0,
            probabilita=100 - i*2
        )
        db.session.add(new_row)
    db.session.commit()
    return jsonify({'success': True})

# Rename previous /start to /home
@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
           """ new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')"""

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  


    return jsonify({})
