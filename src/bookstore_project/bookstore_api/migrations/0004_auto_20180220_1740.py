# Generated by Django 2.0.2 on 2018-02-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0003_auto_20180220_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file_type',
            field=models.CharField(choices=[('EB', 'eBook'), ('AU', 'Audio'), ('NP', 'Newspaper')], default='EB', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('SP', 'Spanish'), ('JP', 'Japanese')], default='EN', max_length=2),
        ),
    ]
