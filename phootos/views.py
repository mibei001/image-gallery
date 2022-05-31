from django.shortcuts import render
from .models import Image, Location , Category
# from django.http  import HttpResponse

# Create your views here.


def image(request):
    images = Image.objects.all()
    print(images)
    return  render (request,'image.html',{"images":images})
    
def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        print(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location(request, location):
    image= Image.filter_by_location(location)
    location= Location.objects.all()
    return render(request, 'location.html',{"location":location, "image":image})      