# Generated by Django 4.1.5 on 2023-01-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='comments',
            name='telefon',
            field=models.CharField(default='telefon', max_length=100, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]
