from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from excel_parser.models import ExcelDocument
from excel_parser.versions.v_1_0.serializers import ExcelDocumentUploadSerializer, ExcelDocumentSerializer


class ExcelDocumentUploadAPIView(CreateAPIView):
    '''
    API (v 1.0) представление для загрузки файла на обработку
    '''
    queryset = ExcelDocument
    serializer_class = ExcelDocumentUploadSerializer
    permission_classes = [IsAuthenticated]


class ExcelDocumentListAPIView(ListAPIView):
    '''
    API (v 1.0) представление для получения списка файлов и их статусов
    '''
    queryset = ExcelDocument.objects.all()
    serializer_class = ExcelDocumentSerializer
    permission_classes = [IsAuthenticated]


class ExcelDocumentAPIView(RetrieveAPIView):
    '''
    API (v 1.0) представление для получения информации о документе
    '''
    queryset = ExcelDocument.objects.all()
    serializer_class = ExcelDocumentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
