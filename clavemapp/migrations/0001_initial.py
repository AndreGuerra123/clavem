# Generated by Django 2.1.4 on 2018-12-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Short title of the product.', max_length=50, verbose_name='Title')),
                ('description', models.TextField(help_text='Longer description of the product.', verbose_name='Description')),
                ('cost', models.DecimalField(decimal_places=2, help_text='Cost of the product without taxes and shipping costs.', max_digits=10, verbose_name='Cost')),
                ('stock', models.IntegerField(default=0, help_text='Amount of product units in stock.', verbose_name='Stock')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Product creation date.', verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='Product modification date.', verbose_name='Date Modified')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(help_text='Caption of the image.', max_length=50, verbose_name='Caption')),
                ('figure', models.ImageField(help_text='Image figure.', upload_to='figures', verbose_name='Figure')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Image creation date.', verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='Image modification date.', verbose_name='Date Modified')),
                ('product', models.ForeignKey(help_text='Product related to image.', on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='clavemapp.Product', verbose_name='Product')),
            ],
        ),
    ]
