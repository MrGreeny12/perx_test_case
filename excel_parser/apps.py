from django.apps import AppConfig


class ExcelParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excel_parser'

    def ready(self):
        import excel_parser.signals
