import logging

from project_config.celery import app

from excel_parser.services.parser_services import Document

logger = logging.getLogger(__name__)


@app.task(bind=True)
def document_processing(self, document_id: str):
    '''
    Задача по обработке документа
    '''
    try:
        document = Document(document_id=document_id)
        document.get_result()
    except Exception as ex:
        logger.debug(ex)
        raise self.retry(exc=ex)
