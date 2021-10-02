# Generated by Django 3.2.7 on 2021-10-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wheater',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(default='2021-10-02', max_length=20)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=6)),
                ('lon', models.DecimalField(decimal_places=4, max_digits=6)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('temperatures', models.TextField()),
            ],
            options={
                'verbose_name': 'Wheater',
                'verbose_name_plural': 'Wheaters',
            },
        ),
    ]