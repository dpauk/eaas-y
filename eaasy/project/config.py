class BaseConfig:
    TESTING = False
    SECRET_KEY = 'i_really_need_to_be_changed'


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
