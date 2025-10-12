import sqlite3

conn = sqlite3.connect('instance/database.db')
c = conn.cursor()

# Add the missing columns to user table
c.execute("ALTER TABLE user ADD COLUMN color_facile_correct VARCHAR(7) DEFAULT '#a7f3bf'")
c.execute("ALTER TABLE user ADD COLUMN color_facile_wrong VARCHAR(7) DEFAULT '#ffb6c1'")
c.execute("ALTER TABLE user ADD COLUMN color_normale_correct VARCHAR(7) DEFAULT '#bfff00'")
c.execute("ALTER TABLE user ADD COLUMN color_normale_wrong VARCHAR(7) DEFAULT '#e53935'")
c.execute("ALTER TABLE user ADD COLUMN color_difficile_correct VARCHAR(7) DEFAULT '#43ea7f'")
c.execute("ALTER TABLE user ADD COLUMN color_difficile_wrong VARCHAR(7) DEFAULT '#800020'")

conn.commit()
conn.close()

print("Columns added successfully!")
