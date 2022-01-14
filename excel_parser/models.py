import datetime

from django.db import models

from excel_parser.services.models_services import ExcelDocumentValidator


class DocumentProcessingStatuses(models.TextChoices):
    DOWNLOAD = 'DOWNLOAD', 'Загружено'
    IN_PROCESS = 'IN_PROCESS', 'Обрабатывается'
    PROCESS_FINISHED = 'PROCESS_FINISHED', 'Обработано'


document_validator = ExcelDocumentValidator(
    content_types=('application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
)


class ExcelDocument(models.Model):
    '''
    Модель документа
    '''
    title = models.CharField(max_length=512, verbose_name='Название')
    document = models.FileField(upload_to='documents/excel_format/', validators=[document_validator], verbose_name='Документ')
    load_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    processing_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания обработки')
    processing_status = models.CharField(max_length=20, choices=DocumentProcessingStatuses.choices,
                                         verbose_name='Статус обработки')
    processing_result = models.CharField(max_length=512, null=True, blank=True, verbose_name='Результат')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.document
            self.processing_status = DocumentProcessingStatuses.DOWNLOAD
        super(ExcelDocument, self).save(*args, **kwargs)

    def save_result(self, result: str):
        if not result:
            self.processing_result = 'Данные обработались некорректно'
        else:
            self.processing_result = result
        self.processing_status = DocumentProcessingStatuses.PROCESS_FINISHED
        self.processing_at = datetime.datetime.now()
        self.save()

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        db_table = 'excel_documents'
        indexes = [
            models.Index(fields=['title'])
        ]
