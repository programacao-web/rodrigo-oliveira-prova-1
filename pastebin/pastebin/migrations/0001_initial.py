# Generated by Django 2.0.4 on 2018-05-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]