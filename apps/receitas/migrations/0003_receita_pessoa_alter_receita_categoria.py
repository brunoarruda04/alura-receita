# Generated by Django 4.0.4 on 2022-06-02 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_rename_date_receita_receita_data_receita'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='categoria',
            field=models.CharField(choices=[('DS', 'Doces e Sobremesas'), ('S', 'Sopas'), ('B', 'Bebidas'), ('M', 'Massas'), ('L', 'Lanches'), ('O', 'Outros')], max_length=2),
        ),
    ]
