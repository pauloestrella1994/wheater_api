from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wheater',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(default='2021-10-02', max_length=20)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('temperatures', models.JSONField()),
            ],
            options={
                'verbose_name': 'Wheater',
                'verbose_name_plural': 'Wheaters',
            },
        ),
    ]
