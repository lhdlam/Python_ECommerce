# Generated by Django 3.1 on 2023-08-02 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100),
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='store/products')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name': 'productgallery',
                'verbose_name_plural': 'product gallery',
            },
        ),
    ]
