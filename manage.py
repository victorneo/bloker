from flask.ext.script import Manager
from bloker import create_app


app = create_app('settings')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()