# Generated by Django 3.2.18 on 2023-05-05 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('datastore_admin', 'Data Store Admin'), ('datastore_create', 'Create DataStore Databases and Collections')),
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatabasePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=255)),
                ('isPublic', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=255)),
                ('isPublic', models.BooleanField(default=True)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='data_store.databasepermission')),
            ],
            options={
                'unique_together': {('collection_name', 'database')},
            },
        ),
    ]