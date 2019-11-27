from django.db import models

# Create your models here.
class Post(models.Model):
	user_name = models.CharField(max_length=100, null=False)
	post_title = models.CharField(max_length=100, null=False)
	post_content = models.TextField(default='tutorial content')
	Post_pub = models.DateField(blank=True, null=True)
	user_profile_link = models.URLField(blank= True,null=True)