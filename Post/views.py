from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Blog
from .forms import UpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

class PostListView(generic.ListView):
    model = Blog
    template_name = 'home.html'
    ordering = '-date_updated'
    paginate_by = 6
    # context_object_name = 'posts'

class PostDetailView(generic.View):
    def get(self, request, slug):
        is_valid_author = False
        object = Blog.objects.filter(slug = slug)[0]
        if object.author == self.request.user:
            is_valid_author = True
        return render(request, 'post_detail.html', {'object':object, 'is_valid_author':is_valid_author})    


class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    model = Blog
    fields = ['title', 'content', 'image']
    success_message = f"Post has been sucessfully created"
    template_name = 'create_post.html'

    # assigning the author of post in form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Blog
    fields = ['title', 'content', 'image']
    template_name = 'create_post.html'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False    


class PostDeleteView(UserPassesTestMixin,SuccessMessageMixin , generic.DeleteView):
    model = Blog
    template_name='delete_post.html'
    success_url = '/'
    success_message = f"Post has been sucessfully deleted"
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False    


# view function for searching the queries
def SearchView(request):
    query = request.GET.get('query')
    posts=[]
    if query is not None:
        titlequery = Blog.objects.filter(title__icontains=query)
        contentquery = Blog.objects.filter(content__icontains=query)
        posts = titlequery.union(contentquery)

    context = {'posts':posts}
    return render(request, 'search.html', context)  



'''
-> using function view for update
def PostUpdateView(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    form = UpdateForm(request.POST or None,request.FILES or None, instance = post)
    if form.is_valid():
        form.save()
        print(f'URL{form.instance.get_absolute_url}')
        return reverse(form.instance.get_absolute_url)

    return render(request, 'create_post.html', {'form':form} )    

    '''

    #make a seperate search html page 




