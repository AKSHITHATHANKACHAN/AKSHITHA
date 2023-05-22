from django.db import models

# Create your models here.

class Product(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_name = models.CharField(max_length=100, blank=True, null=True)
    dbl_rate = models.FloatField(blank=True, null=True)
    int_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

class AddCart(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    fk_product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    int_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_cart'