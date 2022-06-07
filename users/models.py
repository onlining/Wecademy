from django.db import models

class User(TimeStampModel):
    name             = models.CharField(max_length=100)
    email            = models.CharField(max_length=100, unique=True)
    password         = models.CharField(max_length=100)
    mobile_number    = models.CharField(max_length=100)
    profile_image    = models.FileField(upload_to='')
    point            = models.IntegerField()
    coupon           = models.ForeignKey("events.Coupon", on_delete=models.CASCADE)
    kakao_id         = models.CharField(max_length=100)
    github_id        = models.CharField(max_length=100)
    mobile_subscribe = models.BooleanField(default=False)
    email_subscribe  = models.BooleanField(default=False)

    class Meta:
        db_table = "users"

class Tutor(TimeStampModel):
    user = models.ManyToManyField("User", through="TutorLike")

    class Meta:
        db_table = "tutors"

class TutorLike(TimeStampModel):
    tutor    = models.ForeignKey("Tutor", on_delete=models.CASCADE)
    lectures = models.ForeignKey("lectures.Lecture", on_delete=models.CASCADE)

    class Meta:
        db_table = "tutor_likes"

