from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "articles"


class BoardAppConfig(AppConfig):
    name = 'board_app'
