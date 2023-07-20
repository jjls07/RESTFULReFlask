class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:eurocorp@192.168.10.150:3306/td_utp'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:eurocorp@localhost:3306/td_utp'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:eurocorp@localhost:3306/carnetnuevo'
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456789@localhost/carnet_utp"

    # PRODUCCION
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://carnet:dTwM2023@localhost:3306/carnet"
    
    # DEV
    SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "development": DevelopmentConfig,
}