# Generated by Django 4.1.5 on 2023-02-06 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_visit_options_remove_visit_name_visit_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='name',
            field=models.CharField(default='None', max_length=50, verbose_name='Количество: '),
            preserve_default=False,
        ),
    ]