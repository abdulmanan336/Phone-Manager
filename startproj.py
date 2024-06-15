import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

apps = [
  'phone',
  'commands'

]

# Delete migration files
for app in apps:
    migrations_dir = os.path.join(BASE_DIR, app, 'migrations')
    print(migrations_dir)
    if os.path.exists(migrations_dir):
        for filename in os.listdir(migrations_dir):
            file_path = os.path.join(migrations_dir, filename)
            if filename != '__init__.py' and filename.endswith('.py'):
                os.unlink(file_path)

db_file = 'db.sqlite3'

if os.path.exists(db_file):
    os.remove(db_file)
    print(f'{db_file} deleted successfully')
    
# Run Django commands to create new migrations
os.system('pip install -r requirements.txt')
os.system('py manage.py makemigrations')
os.system('py manage.py migrate --fake-initial')
os.system('py manage.py create_superuser')




os.system('py manage.py runserver')
