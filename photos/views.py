from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})



def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

 def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        photos = Photo.objects.filter(
            category__name=searched)

        return render(request,
                      'photos/search_venues.html',
                      {'searched': searched,
                       'photos': photos})

    else:
        return render(request,
                      'photos/search_venues.html',
                      {})


  # Delete a Venue
def delete_venue(request, photo_id):
    venue = Photo.objects.get(pk=photo_id)
    venue.delete()
    return redirect('gallery')                    
   







