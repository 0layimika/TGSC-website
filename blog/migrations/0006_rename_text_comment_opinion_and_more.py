# Generated by Django 4.2.6 on 2023-10-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='opinion',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.TextField(default='boy'),
            preserve_default=False,
        ),
    ]
