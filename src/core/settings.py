from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    TITLE: str = ""


class ProductionConfig(BaseConfig):
    DEBUG: bool = False


class DevelopmentConfig(BaseConfig):

    DEBUG: bool = True

    class Config:
        case_sensitive = True
        env_file = ".env.development"


dev_config = DevelopmentConfig()

if __name__ == "__main__":
    x = DevelopmentConfig()
    print(x.__dict__)