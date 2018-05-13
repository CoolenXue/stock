from database import Database

with Database(log = 'error.log') as db:
    db.debug_en = True
    db.update()
