from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db

import json

views = Blueprint('views', __name__)


@views.route('/')
def start():
    from flask_login import current_user
    return render_template('start.html', user=current_user)

# Route per la tabella
@views.route('/tabella')
def tabella():
    from flask_login import current_user
    return render_template('tabella.html', user=current_user)

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