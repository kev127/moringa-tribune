# Generated by Django 3.1.3 on 2020-11-18 05:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_newsletterrecipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
