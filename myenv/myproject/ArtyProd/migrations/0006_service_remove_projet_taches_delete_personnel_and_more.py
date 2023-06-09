# Generated by Django 4.2 on 2023-04-29 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0005_projet_terminee_tache_en_avance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('categorie', models.CharField(choices=[('CG', 'Charte graphique'), ('O3D', 'Objet 3D'), ('SC', 'Scénarisation')], max_length=3)),
                ('img', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='projet',
            name='taches',
        ),
        migrations.DeleteModel(
            name='Personnel',
        ),
        migrations.DeleteModel(
            name='Projet',
        ),
        migrations.DeleteModel(
            name='Tache',
        ),
    ]
