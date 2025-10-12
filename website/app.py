# migrate_add_columns.py
from website import create_app, db
from sqlalchemy import text

app = create_app()
with app.app_context():
    conn = db.session.connection()
    stmts = [
        "ALTER TABLE user ADD COLUMN color_facile_correct TEXT;",
        "ALTER TABLE user ADD COLUMN color_facile_wrong TEXT;",
        "ALTER TABLE user ADD COLUMN color_normale_correct TEXT;",
        "ALTER TABLE user ADD COLUMN color_normale_wrong TEXT;",
        "ALTER TABLE user ADD COLUMN color_difficile_correct TEXT;",
        "ALTER TABLE user ADD COLUMN color_difficile_wrong TEXT;",
    ]
    for s in stmts:
        try:
            conn.execute(text(s))
            print("Eseguito:", s)
        except Exception as e:
            print("Saltata / Errore su:", s, " -> ", e)
    db.session.commit()
    # Aggiorna valori NULL con valori di default (opzionale)
    try:
        conn.execute(text("UPDATE user SET color_facile_correct='#a7f3bf' WHERE color_facile_correct IS NULL;"))
        conn.execute(text("UPDATE user SET color_facile_wrong='#ffb6c1' WHERE color_facile_wrong IS NULL;"))
        conn.execute(text("UPDATE user SET color_normale_correct='#bfff00' WHERE color_normale_correct IS NULL;"))
        conn.execute(text("UPDATE user SET color_normale_wrong='#e53935' WHERE color_normale_wrong IS NULL;"))
        conn.execute(text("UPDATE user SET color_difficile_correct='#43ea7f' WHERE color_difficile_correct IS NULL;"))
        conn.execute(text("UPDATE user SET color_difficile_wrong='#800020' WHERE color_difficile_wrong IS NULL;"))
        db.session.commit()
        print("Aggiornati i valori NULL con i default.")
    except Exception as e:
        print("Errore aggiornamento default:", e)
