import os


def load_config():
    mode = os.environ.get('FLASK_ENV', 'default')

    if mode == 'production':
        from config.production import ProductionConfig
        return ProductionConfig
    elif mode == 'development':
        from config.development import DevelopmentConfig
        return DevelopmentConfig
    elif mode == 'default':
        from config.development import DevelopmentConfig
        return DevelopmentConfig
