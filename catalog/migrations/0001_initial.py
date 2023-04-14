# Generated by Django 3.2.18 on 2023-04-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('catalog_admin', 'Catalog Admin'), ('catalog_create', 'Create Catalog Collections')),
                'managed': False,
            },
        ),
    ]
