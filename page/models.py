from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class todoModel(models.Model):
	title = models.CharField(max_length=20,blank=True,null=True)
	discription = models.TextField(null=True)
	user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
	created = models.DateTimeField(default=timezone.now)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering=['completed']