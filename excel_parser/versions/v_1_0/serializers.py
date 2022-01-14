from rest_framework.serializers import ModelSerializer

from excel_parser.models import ExcelDocument


class ExcelDocumentUploadSerializer(ModelSerializer):
    class Meta:
        model = ExcelDocument
        fields = ['document']


class ExcelDocumentSerializer(ModelSerializer):
    class Meta:
        model = ExcelDocument
        fields = '__all__'
