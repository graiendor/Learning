# Generated by Django 4.0.6 on 2022-07-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_roll_result_alter_roll_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributes',
            name='charisma_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='composure_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='dexterity_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='intelligence_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='manipulation_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='resolve_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='stamina_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='strength_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attributes',
            name='wits_check',
            field=models.BooleanField(default=False),
        ),
    ]