# Generated by Django 4.2.2 on 2023-07-02 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_statusmodel_name'),
        ('tasks', '0002_alter_tasksmodel_executor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='status_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='status',
                to='statuses.statusmodel'),
        ),
    ]
