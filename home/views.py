from django.shortcuts import render
from django.views.generic import ListView
from users.models import Post

# Create your views here.
def home(request):
	post  =Post.objects.all()
	return render (request, "home_page.html", {'post':post })

class PostListView(ListView):
	model = Post
	template_name = 'home_page.html'
	context_object_name = 'post'
	ordering = ['-Post_pub']