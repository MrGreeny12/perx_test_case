from django.urls import path

from excel_parser.versions.v_1_0.views import ExcelDocumentUploadAPIView, ExcelDocumentListAPIView, ExcelDocumentAPIView

urlpatterns = [
    path('upload/', ExcelDocumentUploadAPIView.as_view(), name='upload_document_url'),
    path('documents/', ExcelDocumentListAPIView.as_view(), name='documents_url'),
    path('document/<int:id>/status/', ExcelDocumentAPIView.as_view(), name='document_status_url')
]
