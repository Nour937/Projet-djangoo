# Generated by Django 4.2 on 2023-05-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0012_tache_personnel_alter_tache_assignee_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='personnel',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.personnel'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='projet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ArtyProd.projet'),
        ),
    ]