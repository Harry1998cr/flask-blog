import os
import logging
from app import create_app
from app import db,init_db
from app.models import User,Role
# from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_login import login_required, current_user
from flask import render_template


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# manager = Manager(app)
# migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
# @manager.command
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def main_page():
    if current_user.is_authenticated:
        return render_template('main_page.html')
    return render_template('welcome_page.html')


if __name__ == '__main__':
    # manager.run()
    with app.app_context():
        create_tables()
        app.logger.setLevel(logging.DEBUG)
        app.run(debug=True)
