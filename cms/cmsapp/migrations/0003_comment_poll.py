# Generated by Django 2.0.4 on 2018-04-04 08:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_auto_20180404_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('poll_num', models.IntegerField(default=0)),
                ('article', models.ForeignKey(null=True, on_delete=True, to='cmsapp.Article')),
                ('user', models.ForeignKey(null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(null=True, on_delete=True, to='cmsapp.Article')),
                ('comment', models.ForeignKey(null=True, on_delete=True, to='cmsapp.Comment')),
                ('user', models.ForeignKey(null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
