import os

from apps import create_app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', default='default'))
    app.run()
