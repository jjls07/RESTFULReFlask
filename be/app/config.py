class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/reactrestful'


    
    # DEV
    SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "development": DevelopmentConfig,
}
