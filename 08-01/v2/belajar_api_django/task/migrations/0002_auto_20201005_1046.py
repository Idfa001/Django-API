# Generated by Django 3.1.2 on 2020-10-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('motto', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='laptop',
        ),
    ]
