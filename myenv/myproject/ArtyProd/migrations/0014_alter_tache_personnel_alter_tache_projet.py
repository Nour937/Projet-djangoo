# Generated by Django 4.2 on 2023-05-16 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0013_alter_tache_personnel_alter_tache_projet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='personnel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ArtyProd.personnel'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='projet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ArtyProd.projet'),
        ),
    ]
