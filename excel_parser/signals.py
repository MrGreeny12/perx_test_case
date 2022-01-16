from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from excel_parser.models import ExcelDocument
from excel_parser.tasks import document_processing


@receiver(post_save, sender=ExcelDocument)
def create_new_excel_document(sender, instance, created, **kwargs):
    document_processing.delay(document_id=instance.id)


@receiver(post_delete, sender=ExcelDocument)
def delete_new_excel_document(sender, instance, **kwargs):
    instance.document.delete(save=False)
