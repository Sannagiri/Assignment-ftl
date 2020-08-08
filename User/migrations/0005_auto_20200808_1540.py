# Generated by Django 3.1 on 2020-08-08 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20200808_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_periods', to='User.user'),
        ),
    ]
