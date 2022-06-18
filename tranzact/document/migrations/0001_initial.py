# Generated by Django 4.0.5 on 2022-06-18 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('file', models.FileField(upload_to='document/')),
                ('tnc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('version', models.SmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesQuotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='document/')),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nclient')),
                ('tnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.tnc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='document/')),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.FloatField()),
                ('delivery_date', models.DateTimeField()),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('product', models.CharField(choices=[('Steel', 'steel'), ('Spring', 'spring')], max_length=50)),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nsource')),
                ('tnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.tnc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='document/')),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.PositiveIntegerField()),
                ('delivery_date', models.DateTimeField()),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nclient')),
                ('tnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.tnc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InwardDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='document/')),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nsource')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.purchaseorder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='document/')),
                ('doc_type', models.CharField(choices=[('purchase_order', 'PurchaseOrder'), ('sales_quote', 'SalesQuote'), ('invoice', 'Invoice'), ('order_confirmation', 'OrderConfirmation'), ('inward_document', 'InwardDocument'), ('tnc', 'TnC')], max_length=50)),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('n_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.nclient')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.orderconfirmation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]