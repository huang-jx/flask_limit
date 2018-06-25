from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from app import create_app

app_init = create_app()
manager = Manager(app=app_init)

manager.add_command('start', Server(host='127.0.0.1', port=8888))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
