from django.db import models

# Create your models here.


class Location(models.Model):
    location= models.CharField(max_length =30)

    def __str__(self):
        return self.location
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        location = Location.objects.filter_by(id = 2).update(location = 'kigali')

class Category(models.Model):
    category = models.CharField(max_length =30)

    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

    def update_category(self):
        category = Category.objects.filter_by(id = 2).update(category = 'sport')

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null=True)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    location =  models.ForeignKey(Location, null=True)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        images = Image.objects.filter_by(id = 2).update(name = 'animal')

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,location):
        image = cls.objects.filter(location__location__icontains = location)
        return image    

