from django.db import models

# Create your models here.

# medical records database

class patient(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField()
	medication = models.CharField(max_length=100)

class doctor(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField()

def user_directory_path(instance, filename):
	
	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
	return 'user_{0}/{1}'.format(instance.patient.id, filename)
	


class Records(models.Model):
	id = models.IntegerField(primary_key=True, auto_created=True)
	patient = models.ForeignKey('patient', on_delete=models.CASCADE)
	doctor = models.ForeignKey('doctor', on_delete=models.CASCADE)
	document = models.FileField(upload_to = user_directory_path)
	time_limit = models.DateTimeField(null=True, blank=True)
	approval_doc = models.CharField(max_length=1, default="B") # Y or N or B B is blank # for the doctor
	approval_rec = models.CharField(max_length=1, default="B") # Y or N or B B is blank # for the record


