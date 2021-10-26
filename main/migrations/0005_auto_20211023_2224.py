# Generated by Django 3.0.3 on 2021-10-23 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20211021_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='category',
            field=models.CharField(choices=[('WITHDRAWAL', 'WITHDRAWAL'), ('TRANSFER', 'TRANSFER'), ('LUCKY', 'LUCKY'), ('COMMISSION', 'COMMISSION'), ('TOP-UP', 'TOP-UP'), ('REGISTRATION', 'REGISTRATION')], max_length=20),
        ),
        migrations.CreateModel(
            name='TopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Convert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
