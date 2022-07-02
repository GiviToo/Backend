# Generated by Django 4.0.5 on 2022-07-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_projectregistrant_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectregistrant',
            name='status',
            field=models.CharField(choices=[('UNASSIGNED', 'Unassigned'), ('ASSIGNED', 'Assigned'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished'), ('CANCELED', 'Canceled')], default='UNASSIGNED', max_length=11),
        ),
    ]
