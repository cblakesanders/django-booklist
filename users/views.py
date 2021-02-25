from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Relationship


from serializers import RelationshipSerializer
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response



def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {'form':form})

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form, 
        'p_form': p_form, 
        
    }
    return render(request, "users/update_profile.html", context)

class profile_view(TemplateView):
    model = Profile
    template_name = 'users/profile.html'
    

    def get_username(self, *args, **kwargs):
        username = self.kwargs.get('username')
        return username

    def get_profile(self, *args, **kwargs):
        username = self.get_username()
        profile = User.objects.get(username=username)
        return profile

    def get_following_count(self, *args, **kwargs):
        username = self.get_username()
        following = Relationship.objects.filter(followingUser__username=username).count()
        return following

    def get_followers_count(self, *args, **kwargs):
        username = self.get_username()
        followers = Relationship.objects.filter(followerUser__username=username).count()
        return followers

    # def post(self, request, *args, **kwargs):
    #     print("here")
    #     print(request.user)
    #     return JsonResponse({'foo': 'bar'})
        

    def get_context_data(self, *args, **kwargs):
        context = super(profile_view, self).get_context_data(**kwargs)

        following = self.get_following_count()
        
        followers = self.get_followers_count()
        
        profile = self.get_profile()

        context.update({'following': following, 'followers': followers, 'profile': profile})
        return context

@api_view(['POST'])
def update_relationship_view(request):
    data = request.data
    
    followingUser = User.objects.get(username=data['followingUser'])
    print(type(followingUser))
    followerUser = User.objects.get(username=data['followerUser'])
    print(type(followerUser))
    Relationship.objects.create(followerUser=followerUser, followingUser=followingUser, status=1)
   
    return Response({'message': 'hello, world'})

