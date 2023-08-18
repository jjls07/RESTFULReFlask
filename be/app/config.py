import os

class Config:
    pass


class ProductionConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_DB_CONN')

class DevelopmentConfig(Config):
    DEBUG = True


    # SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_DB_CONN')


    
    # DEV
    SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "development": DevelopmentConfig,
}
