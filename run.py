from dotenv import load_dotenv
from os.path import join, dirname
from app.databases.database import Database
import os
from app.views import create_app
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)



psswd =  os.getenv("ADMIN_PASSWORD")
eml = os.getenv("ADMIN_EMAIL")

app = create_app('development')

database = Database()
database.create_all_tables()
database.create_default_admin(eml, psswd)

if __name__ == '__main__':
    app.run()
