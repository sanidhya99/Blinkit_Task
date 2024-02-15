# Generated by Django 4.2.3 on 2024-02-15 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0005_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('notes', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='friends',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='subject',
        ),
        migrations.DeleteModel(
            name='block',
        ),
        migrations.DeleteModel(
            name='comments',
        ),
        migrations.DeleteModel(
            name='friends',
        ),
        migrations.DeleteModel(
            name='post',
        ),
        migrations.DeleteModel(
            name='requests',
        ),
    ]