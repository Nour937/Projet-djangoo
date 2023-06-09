# Generated by Django 4.2 on 2023-05-18 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0015_alter_tache_personnel_alter_tache_projet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tache',
            name='assignee_a',
            field=models.ManyToManyField(blank=True, related_name='assigned_taches', to='ArtyProd.personnel'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taches', to='ArtyProd.personnel'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taches', to='ArtyProd.projet'),
        ),
    ]
