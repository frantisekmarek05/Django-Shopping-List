# Generated by Django 2.1.7 on 2025-05-27 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0006_auto_20250518_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemslist',
            name='category',
            field=models.CharField(choices=[('dairy', 'Mléčné výrobky'), ('vegetables', 'Ovoce a zelenina'), ('frozen', 'Mražené potraviny'), ('meal', 'Hotová jídla'), ('bread', 'Pečivo'), ('other', 'Ostatní')], default='other', help_text='Category of the shopping item', max_length=20),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='completed',
            field=models.BooleanField(default=False, help_text='Whether the item has been purchased'),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the item was added'),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='description',
            field=models.TextField(blank=True, help_text='Optional description of the item', null=True),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='image',
            field=models.ImageField(blank=True, help_text='Optional image of the item', null=True, upload_to='items_images/'),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='itemname',
            field=models.CharField(help_text='Name of the shopping item', max_length=200),
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='user',
            field=models.ForeignKey(help_text='User who owns this item', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
