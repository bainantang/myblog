# Generated by Django 2.2.8 on 2020-04-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_put_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='put_time',
            field=models.DateTimeField(null=True),
        ),
    ]