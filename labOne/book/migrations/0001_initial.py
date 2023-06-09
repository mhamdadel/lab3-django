# Generated by Django 4.2 on 2023-04-09 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(blank=True, null=True)),
                ('pageNumbers', models.IntegerField()),
                ('category', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('funny', 'Funny'), ('science_fiction', 'Science Fiction')], max_length=20)),
                ('iscompleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
