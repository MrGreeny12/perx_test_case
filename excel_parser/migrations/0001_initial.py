# Generated by Django 4.0.1 on 2022-01-14 06:46

from django.db import migrations, models
import excel_parser.services


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Название')),
                ('document', models.FileField(upload_to='documents/excel_format/', validators=[excel_parser.services.models_services.ExcelDocumentValidator(content_types=('application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))], verbose_name='Документ')),
                ('load_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('processing_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания обработки')),
                ('processing_status', models.CharField(choices=[('DOWNLOAD', 'Загружено'), ('IN_PROCESS', 'Обрабатывается'), ('PROCESS_FINISHED', 'Обработано')], max_length=20, verbose_name='Статус обработки')),
                ('processing_result', models.CharField(blank=True, max_length=512, null=True, verbose_name='Результат')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'db_table': 'excel_documents',
            },
        ),
        migrations.AddIndex(
            model_name='exceldocument',
            index=models.Index(fields=['title'], name='excel_docum_title_3375c1_idx'),
        ),
    ]
