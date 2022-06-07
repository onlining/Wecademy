from django.db   import models

from cors.models import TimeStampedModel

class User(TimeStampedModel):
    name             = models.CharField(max_length=100, null=True)
    email            = models.CharField(max_length=100, unique=True)
    password         = models.CharField(max_length=100, null=True)
    kakao_id         = models.BigIntegerField(null=True)
    github_id        = models.CharField(max_length=100, null=True)
    google_id        = models.CharField(max_length=100, null=True)
    naver_id         = models.CharField(max_length=100, null=True)
  
    class Meta:
        db_table = "users"

class UserInformation(TimeStampedModel):
    mobile_number    = models.CharField(max_length=100)
    profile_image    = models.URLField()
    point            = models.IntegerField(null=True)
    coupon           = models.ForeignKey("events.Coupon", on_delete=models.CASCADE, null=True)
    mobile_subscribe = models.BooleanField(default=False)
    email_subscribe  = models.BooleanField(default=False)

    class Meta:
        db_table = "user_informations"

class Tutor(TimeStampedModel):
    user = models.ManyToManyField("User", through="TutorLike")

    class Meta:
        db_table = "tutors"

class TutorLike(TimeStampedModel):
    tutor    = models.ForeignKey("Tutor", on_delete=models.CASCADE)
    user     = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = "tutor_likes"

