from app.databases.database import Database
import os
from app.views import create_app

app = create_app('development')

database = Database()
database.create_all_tables()

if __name__ == '__main__':
    app.run()
