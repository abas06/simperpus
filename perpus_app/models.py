
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class MasterBuku(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama_buku = models.CharField(max_length=256, blank=True, null=True)
    penulis = models.CharField(max_length=256, blank=True, null=True)
    sumber_buku = models.ForeignKey('MasterSumberBuku', models.DO_NOTHING)
    harga_beli = models.FloatField(blank=True, null=True)
    harga_jual = models.FloatField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    harga_sewa = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False  # Ubah menjadi True jika Anda ingin Django mengelola tabel
        db_table = 'master_buku'
        
class MasterMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_member = models.CharField(max_length=256, blank=True, null=True)
    jenis_identitas = models.SmallIntegerField(blank=True, null=True)
    no_identitas = models.CharField(max_length=256, blank=True, null=True)
    nama = models.CharField(max_length=256, blank=True, null=True)
    alamat_ktp = models.CharField(max_length=256, blank=True, null=True)
    domisili = models.CharField(max_length=256, blank=True, null=True)
    status_aktif = models.BooleanField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_member'

class MasterSumberBuku(models.Model):
    id_sumber = models.BigAutoField(primary_key=True)
    sumber = models.CharField(max_length=256, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        managed = False  # Ubah menjadi True jika Anda ingin Django mengelola tabel
        db_table = 'master_sumber_buku'
    
class TransaksiKunjungan(models.Model):
    id = models.BigAutoField(primary_key=True)
    member_id = models.ForeignKey(MasterMember, models.DO_NOTHING, db_column='member_id', blank=True, null=True)
    jenis_transaksi = models.SmallIntegerField(blank=True, null=True)
    tgl_transaksi = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    no_transaksi = models.CharField(max_length=256, blank=True, null=True)
    jenis_kunjungan = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaksi_kunjungan'

class BillingKasir(models.Model):
    id = models.BigAutoField(primary_key=True)
    kunjungan_id = models.ForeignKey(TransaksiKunjungan, models.DO_NOTHING, db_column='kunjungan_id', blank=True, null=True)
    no_billing = models.CharField(max_length=256, blank=True, null=True)
    total_billing = models.FloatField(blank=True, null=True)
    tgl_transaksi = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_kasir'

class BillingKasirDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    billing_id = models.IntegerField(models.DO_NOTHING, blank=True, null=True)
    buku_id = models.IntegerField(blank=True, null=True)
    jenis_transaksi = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    hari_peminjaman = models.IntegerField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_kasir_detail'
        