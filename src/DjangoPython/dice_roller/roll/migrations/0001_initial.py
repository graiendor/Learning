# Generated by Django 4.0.6 on 2022-07-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(editable=False)),
                ('result', models.CharField(editable=False, max_length=8)),
            ],
        ),
    ]