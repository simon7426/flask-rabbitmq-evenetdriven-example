class BaseConfig:
    TESTING = False
    SECRET_KEY = "poridhi"
    RABBITMQ_HOST = "rabbitmq"
    RABBITMQ_USER = "poridhi"
    RABBITMQ_PASSWORD = "poridhi"


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
