# Generated by Django 4.2.6 on 2023-10-30 15:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='opinion',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
            preserve_default=False,
        ),
    ]