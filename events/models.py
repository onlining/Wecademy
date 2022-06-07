from django.db import models

class Coupon(TimeStampModel):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "coupons"

class Package(TimeStampModel):
    name             = models.CharField(max_length=30)
    lecture          = models.ForeignKey("lectures.Lecture", on_delete=models.CASCADE)
    discount_percent = models.DecimalField(max_digits = 3, decimal_places = 2)
    
    class Meta:
        db_table = "packages"