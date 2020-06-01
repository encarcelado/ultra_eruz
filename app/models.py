# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from django.shortcuts import reverse


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BossPerson(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    f_name = models.CharField(max_length=50)
    s_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=70)
    phone_1 = models.CharField(max_length=50)
    phone_2 = models.CharField(max_length=50)
    phone_3 = models.CharField(max_length=50)
    cellphone_1 = models.CharField(max_length=50)
    cellphone_2 = models.CharField(max_length=50)
    cellphone_3 = models.CharField(max_length=50)
    email_1 = models.CharField(max_length=100)
    email_2 = models.CharField(max_length=100)
    email_3 = models.CharField(max_length=100)
    boss_inn = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'boss_person'


class ContractCard(models.Model):
    contract_num = models.CharField(unique=True, max_length=30, blank=True, null=True)
    status_kontrakta = models.CharField(max_length=50, blank=True, null=True)
    price_kontrakta = models.CharField(max_length=50, blank=True, null=True)
    data_zakl_kontrakta = models.CharField(max_length=50, blank=True, null=True)
    data_ispol_kontrakta = models.CharField(max_length=50, blank=True, null=True)
    data_end_kontrakta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_card'


class ContractCardOkpd(models.Model):
    contract_card_id = models.IntegerField(primary_key=True)
    okpd_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contract_card_okpd'
        unique_together = (('contract_card_id', 'okpd_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class TipUchastnika(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tip_uchastnika'

class NalogCodes(models.Model):
    nalog_kod = models.CharField(max_length=4, blank=True, null=True)
    nalog_region = models.CharField(max_length=38, blank=True, null=True)
    nalog_city = models.CharField(max_length=26, blank=True, null=True)
    is_main = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nalog_codes'


class EruzMember(models.Model):
    id = models.AutoField(primary_key=True)
    eruz_registry_id = models.CharField(max_length=9)
    eruz_member_inn = models.CharField(max_length=12)
    foreign_inn = models.CharField(max_length=15)
    registry_date = models.CharField(max_length=12)
    eruz_registry_date = models.CharField(max_length=100)
    ogrnip = models.CharField(max_length=20)
    ogrn = models.CharField(max_length=15)
    nalog_reg_date = models.CharField(max_length=20)
    ip_reg_date = models.CharField(max_length=20)
    company_email = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=255)
    company_cell = models.CharField(max_length=20)
    company_cell2 = models.CharField(max_length=20)
    full_company_name = models.CharField(max_length=255)
    short_company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    company_kpp = models.CharField(max_length=15)
    company_site = models.CharField(max_length=255)
    registry_country = models.CharField(max_length=100)
    registry_status = models.CharField(max_length=15)
    is_filial = models.IntegerField()
    # tip_uchastnika_id = models.IntegerField()
    tip_uchastnika_id = models.ForeignKey(TipUchastnika, on_delete=models.CASCADE, db_column='tip_uchastnika_id')

    # boss_person_id = models.IntegerField()
    boss_person_id = models.ForeignKey(BossPerson, on_delete=models.CASCADE, db_column='boss_person_id')
    nalog_codes_id = models.ForeignKey(NalogCodes, on_delete=models.CASCADE, db_column='nalog_codes_id')
    # nalog_codes_id = models.IntegerField()
    small_business_subject = models.IntegerField()
    main_okved = models.CharField(max_length=20)
    main_okved_desc = models.CharField(max_length=255)



    class Meta:
        managed = False
        db_table = 'eruz_member'


class EruzMemberContractCard(models.Model):
    eruz_member_id = models.CharField(max_length=20)
    contract_card_id = models.CharField(max_length=20)
    win_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'eruz_member_contract_card'


class EruzMemberOkpd(models.Model):
    eruz_member_id = models.CharField(primary_key=True, max_length=10)
    okpd_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'eruz_member_okpd'
        unique_together = (('eruz_member_id', 'okpd_id'),)


class EruzMemberOkvedCodes(models.Model):
    gov_eruz_registry_id = models.IntegerField(primary_key=True)
    okved_codes_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eruz_member_okved_codes'
        unique_together = (('gov_eruz_registry_id', 'okved_codes_id'),)


class EruzMemberZakupkaCard(models.Model):
    eruz_member_id = models.CharField(primary_key=True, max_length=20)
    zakupka_card_id = models.CharField(max_length=20)
    win_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'eruz_member_zakupka_card'
        unique_together = (('eruz_member_id', 'zakupka_card_id', 'win_status'),)




class Okpd22020(models.Model):
    okpd2_code = models.CharField(max_length=15)
    okpd2_desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'okpd2_2020'


class Okved2020(models.Model):
    okved_code = models.CharField(max_length=8)
    okved_desc = models.CharField(max_length=422)

    class Meta:
        managed = False
        db_table = 'okved_2020'





class ZakazchikCard(models.Model):
    full_name_zakazchika = models.CharField(max_length=255, blank=True, null=True)
    short_name_zakazchika = models.CharField(max_length=200, blank=True, null=True)
    date_uchet_zakazchika = models.CharField(max_length=50, blank=True, null=True)
    id_zakazchika = models.CharField(max_length=50, blank=True, null=True)
    inn_zakazchika = models.CharField(max_length=20, blank=True, null=True)
    kpp_zakazchika = models.CharField(max_length=50, blank=True, null=True)
    kod_opf_zakazchika = models.CharField(max_length=50, blank=True, null=True)
    kod_okpo_zakazchika = models.CharField(max_length=50, blank=True, null=True)
    kod_ter_zakazchika = models.CharField(max_length=70, blank=True, null=True)
    zakazchik_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zakazchik_card'


class ZakupkaCard(models.Model):
    zakupka_num = models.CharField(max_length=30)
    ikz = models.CharField(max_length=30)
    zakupka_link = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'zakupka_card'


class ZakupkaCardOkpd(models.Model):
    zakupka_card_id = models.CharField(primary_key=True, max_length=20)
    okpd_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'zakupka_card_okpd'
        unique_together = (('zakupka_card_id', 'okpd_id'),)
