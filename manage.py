import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db 

app.config.from_object(os.environ['APP_ENVIRONMENT'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()


# python manage.py db init

# python manage.py db migrate

# python manage.py db upgrade

# heroku run python manage.py db upgrade --app allstarrma-staging
# heroku run python manage.py db upgrade --app allstarrma-production