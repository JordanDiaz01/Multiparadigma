class BasicConfig:
    USER_DB='postgres'
    PASS_DB='Sobrecarga2*'
    URL_DB='localhost'
    NAME_DB='polloshermanos'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI=FULL_URL_DB
    DEBUG=True
    SECRET_KEY="llave123"
    BCRYPT_LOG_ROUNDS=13
    SQLALCHEMY_TRACK_MODIFICATIONS=False