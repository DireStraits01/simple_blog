# Generated by Django 3.1.4 on 2020-12-31 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0009_auto_20201230_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=255, verbose_name='your comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='first.article', verbose_name='comments'),
        ),
    ]
