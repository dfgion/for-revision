# Generated by Django 4.1.7 on 2023-03-09 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_options_alter_tag_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
    ]
