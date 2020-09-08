from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField()
	year = models.IntegerField()
	teacher= models.ForeignKey(User, default=1, on_delete=models.CASCADE)


	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name=models.CharField(max_length=120)
	dob=models.DateField(default=timezone.now)
	#DateField(auto_now= False , auto_now_add= True)
	#GENDER_CHOICES=["Male", "Female"]
	MALE="Male"
	FEMALE="Female"
	gender= models.CharField( max_length=120, choices=[(MALE,"Male"),(FEMALE, "Female")],)
	exam_grade=models.DecimalField(max_digits=10, decimal_places=3)
	classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE)
	ordering=['name']
