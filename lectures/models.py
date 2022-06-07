from django.db   import models

from cors.models import TimeStampedModel

class Lecture(TimeStampedModel):
    name            = models.CharField(max_length=100)
    information     = models.VarCharField(max_length=2000)
    level           = models.ForeignKey('Level', on_delete = models.CASCADE)
    price           = models.DecimalField(max_digits=8,decimal_places=2)
    tutor           = models.ForeignKey('users.Tutor', on_delete = models.CASCADE)
    thumbnail_image = models.FileField(upload_to='')
    lecture_like    = models.ManyToManyField('users.User')
    tag             = models.ManyToManyField('Tag')
    wish_list       = models.ManyToManyField('users.User')

    class Meta:
        db_table = "lectures"

class Course(models.Model):
    name    = models.CharField(max_length=100)
    lecture = models.ForeignKey('Lecture', on_delete = models.CASCADE)
    
    class Meta:
        db_table = "courses"

class Video(TimeStampedModel):
    name    = models.CharField(max_lenght=100)
    course  = models.ForeignKey('Course', on_delete = models.CASCADE)
    content = models.FileField(upload_to='')
    
    class Meta:
        db_table = "videos"
   
class MainCategory(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "main_category"

class SubCategory(models.Model):
    name          = models.CharField(max_length=30)
    main_category = models.ForeignKey('Lecture', on_delete = models.CASCADE)

    class Meta:
        db_table = "sub_category"

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tags'

class Review(TimeStampModel):
    name    = models.CharField(max_length=30)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    rating  = models.IntegerField()

    class Meta:
        db_table = 'reviews'

class Level(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'levels'
