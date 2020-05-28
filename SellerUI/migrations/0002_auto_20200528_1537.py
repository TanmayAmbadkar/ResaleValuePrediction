# Generated by Django 3.0.5 on 2020-05-28 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SellerUI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('S', 'Seller'), ('C', 'Customer'), ('B', 'Broker')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SellerUI.Profile'),
        ),
        migrations.DeleteModel(
            name='SellerProfile',
        ),
    ]