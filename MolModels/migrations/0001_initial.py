# Generated by Django 2.2.6 on 2019-11-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreateDate', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('Code', models.CharField(max_length=2, verbose_name='国家编码')),
                ('Name', models.CharField(max_length=200, verbose_name='国家名称')),
                ('FlagPictureName', models.CharField(max_length=200, verbose_name='国旗图片名称')),
            ],
            options={
                'verbose_name': 'ModelName',
                'verbose_name_plural': 'ModelNames',
                'db_table': 'tb_Country',
                'managed': True,
            },
        ),
    ]