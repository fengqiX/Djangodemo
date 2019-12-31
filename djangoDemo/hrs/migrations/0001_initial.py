# Generated by Django 2.2.3 on 2019-12-30 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('no', models.IntegerField(db_column='dno', primary_key=True, serialize=False, verbose_name='department NO.')),
                ('name', models.CharField(db_column='dname', max_length=20, verbose_name='department Name')),
                ('location', models.CharField(db_column='dloc', max_length=30, verbose_name='department locations')),
            ],
            options={
                'db_table': 'tb_dept',
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('no', models.IntegerField(db_column='eno', primary_key=True, serialize=False, verbose_name='employee NO.')),
                ('name', models.CharField(db_column='ename', max_length=30, verbose_name='employee name')),
                ('job', models.CharField(max_length=30, verbose_name='positions')),
                ('sal', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='monthly salary')),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='subsidy')),
                ('dept', models.ForeignKey(db_column='dno', on_delete=django.db.models.deletion.PROTECT, to='hrs.Dept', verbose_name='department located')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrs.Emp', verbose_name='Manager')),
            ],
            options={
                'db_table': 'tb_emp',
            },
        ),
    ]