class basicConfigs:
    USER_DB = 'postgres'  # Nombre de usuario de la base de datos
    PASS_DB = 'Sobrecarga2*'  # Contraseña de la base de datos
    URL_DB = 'localhost'  # Dirección de la base de datos
    NAME_DB = 'u2eflask'  # Nombre de la base de datos
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'  # URL completa de la base de datos
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB  # Configuración de la URI de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de las modificaciones a la base de datos

    # Configuración de la llave secreta para proteger la aplicación de ataques CSRF
    SECRET_KEY = "llave secreta"