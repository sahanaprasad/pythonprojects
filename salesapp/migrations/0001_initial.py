# Generated by Django 2.0.6 on 2018-06-19 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.CharField(max_length=5, unique=True)),
                ('cname', models.CharField(max_length=30)),
                ('cadd', models.CharField(max_length=100)),
                ('cpin', models.IntegerField()),
                ('cstate', models.CharField(max_length=50)),
                ('cbal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ono', models.CharField(max_length=5, unique=True)),
                ('odate', models.DateField()),
                ('Oqty', models.IntegerField()),
                ('ototal', models.IntegerField()),
                ('opaystatus', models.BooleanField()),
                ('ocid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pno', models.CharField(max_length=5, unique=True)),
                ('pname', models.CharField(max_length=30)),
                ('pcost', models.IntegerField()),
                ('pmanufacturer', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='opid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salesapp.product'),
        ),
    ]
