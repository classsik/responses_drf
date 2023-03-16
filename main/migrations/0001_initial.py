# Generated by Django 4.1.7 on 2023-03-16 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dad_name', models.CharField(max_length=255)),
                ('username', models.SlugField(unique=True)),
                ('password', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('admin', 'Администратор'), ('cook', 'Повар'), ('waiter', 'Официант')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.IntegerField(verbose_name='Номер столика')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('added', 'Добавлен'), ('in_work', 'Готовится'), ('canceled', 'Отменен'), ('payed', 'Оплачен')], max_length=30)),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post'),
        ),
    ]
