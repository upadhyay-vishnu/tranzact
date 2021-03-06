# Generated by Django 4.0.5 on 2022-06-18 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_remove_customer_product_remove_nclient_product_and_more'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceProductPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nsource')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sourceproduct')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConsumerProductSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nclient')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.consumerproduct')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
