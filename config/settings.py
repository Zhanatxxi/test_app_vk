from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SERVICE_KEY: str
    TOKEN: str

    V: float = 5.131
    BASE_URL: str = "https://api.vk.com/method"
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = Settings()
