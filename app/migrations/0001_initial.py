# Generated by Django 2.1.15 on 2020-04-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BossPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('f_name', models.CharField(max_length=50)),
                ('s_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=70)),
                ('phone_1', models.CharField(max_length=50)),
                ('phone_2', models.CharField(max_length=50)),
                ('phone_3', models.CharField(max_length=50)),
                ('cellphone_1', models.CharField(max_length=50)),
                ('cellphone_2', models.CharField(max_length=50)),
                ('cellphone_3', models.CharField(max_length=50)),
                ('email_1', models.CharField(max_length=100)),
                ('email_2', models.CharField(max_length=100)),
                ('email_3', models.CharField(max_length=100)),
                ('boss_inn', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'boss_person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContractCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_num', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('status_kontrakta', models.CharField(blank=True, max_length=50, null=True)),
                ('price_kontrakta', models.CharField(blank=True, max_length=50, null=True)),
                ('data_zakl_kontrakta', models.CharField(blank=True, max_length=50, null=True)),
                ('data_ispol_kontrakta', models.CharField(blank=True, max_length=50, null=True)),
                ('data_end_kontrakta', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'contract_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ContractCardOkpd',
            fields=[
                ('contract_card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('okpd_id', models.IntegerField()),
            ],
            options={
                'db_table': 'contract_card_okpd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EruzMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eruz_registry_id', models.CharField(max_length=9)),
                ('eruz_member_inn', models.CharField(max_length=12)),
                ('foreign_inn', models.CharField(max_length=15)),
                ('registry_date', models.CharField(max_length=12)),
                ('ogrnip', models.CharField(max_length=20)),
                ('ogrn', models.CharField(max_length=15)),
                ('nalog_reg_date', models.CharField(max_length=20)),
                ('ip_reg_date', models.CharField(max_length=20)),
                ('company_email', models.CharField(max_length=100)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_cell', models.CharField(max_length=20)),
                ('company_cell2', models.CharField(max_length=20)),
                ('full_company_name', models.CharField(max_length=255)),
                ('short_company_name', models.CharField(max_length=255)),
                ('company_address', models.TextField()),
                ('company_kpp', models.CharField(max_length=15)),
                ('company_site', models.CharField(max_length=255)),
                ('registry_country', models.CharField(max_length=100)),
                ('registry_status', models.CharField(max_length=15)),
                ('is_filial', models.IntegerField()),
                ('tip_uchastnika_id', models.IntegerField()),
                ('boss_person_id', models.IntegerField()),
                ('nalog_codes_id', models.IntegerField()),
                ('small_business_subject', models.IntegerField()),
                ('main_okved', models.CharField(max_length=20)),
                ('main_okved_desc', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'eruz_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EruzMemberContractCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eruz_member_id', models.CharField(max_length=20)),
                ('contract_card_id', models.CharField(max_length=20)),
                ('win_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'eruz_member_contract_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EruzMemberOkpd',
            fields=[
                ('eruz_member_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('okpd_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'eruz_member_okpd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EruzMemberOkvedCodes',
            fields=[
                ('gov_eruz_registry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('okved_codes_id', models.IntegerField()),
            ],
            options={
                'db_table': 'eruz_member_okved_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EruzMemberZakupkaCard',
            fields=[
                ('eruz_member_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('zakupka_card_id', models.CharField(max_length=20)),
                ('win_status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'eruz_member_zakupka_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NalogCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nalog_kod', models.CharField(blank=True, max_length=4, null=True)),
                ('nalog_region', models.CharField(blank=True, max_length=38, null=True)),
                ('nalog_city', models.CharField(blank=True, max_length=26, null=True)),
            ],
            options={
                'db_table': 'nalog_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Okpd22020',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okpd2_code', models.CharField(max_length=15)),
                ('okpd2_desc', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'okpd2_2020',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Okved2020',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('okved_code', models.CharField(max_length=8)),
                ('okved_desc', models.CharField(max_length=422)),
            ],
            options={
                'db_table': 'okved_2020',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipUchastnika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tip_uchastnika',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZakazchikCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_zakazchika', models.CharField(blank=True, max_length=255, null=True)),
                ('short_name_zakazchika', models.CharField(blank=True, max_length=200, null=True)),
                ('date_uchet_zakazchika', models.CharField(blank=True, max_length=50, null=True)),
                ('id_zakazchika', models.CharField(blank=True, max_length=50, null=True)),
                ('inn_zakazchika', models.CharField(blank=True, max_length=20, null=True)),
                ('kpp_zakazchika', models.CharField(blank=True, max_length=50, null=True)),
                ('kod_opf_zakazchika', models.CharField(blank=True, max_length=50, null=True)),
                ('kod_okpo_zakazchika', models.CharField(blank=True, max_length=50, null=True)),
                ('kod_ter_zakazchika', models.CharField(blank=True, max_length=70, null=True)),
                ('zakazchik_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'zakazchik_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZakupkaCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakupka_num', models.CharField(max_length=30)),
                ('ikz', models.CharField(max_length=30)),
                ('zakupka_link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'zakupka_card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZakupkaCardOkpd',
            fields=[
                ('zakupka_card_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('okpd_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'zakupka_card_okpd',
                'managed': False,
            },
        ),
    ]
