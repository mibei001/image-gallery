from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new image and saving it
        self.new_image= Image(image ='images/', image_name ='fudu', image_description = "food image")

    # Testing  instance

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

   # Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    #test delete
    def test_delete_image(self):
        self.new_image.save_image()
        image = Image.objects.filter(image_name='fudu').first()
        delete = Image.objects.filter(image_name = image.image_name).delete()
        images = Image.objects.all()
        self.assertFalse(len(images)==1)

    # Testing Update Method
    def test_update_image(self):  
        self.new_image.save_image()
        image = Image.objects.filter(image_name='fudu').first()
        update = Image.objects.filter(image_name=image.image_name).update(image_name='ibiryo')
        updated = Image.objects.filter(image_name='ibiryo').first()
        self.assertNotEqual(image.image_name, updated.image_name)  

    #  Test search method
    def test_search_by_category(self):
        images = Image.objects.all()
        self.assertFalse(len(images)>0)
   
    #  Test search method
    def test_search_by_category(self):
        images = Image.objects.all()
        self.assertFalse(len(images)>0)

    #  Test location method
    def test_filter_by_location(self):
        images = Image.objects.all()
        self.assertFalse(len(images)>0)


class LocationTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.new_location= Location(location = "kimuhurura")
        
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing Save Method
    def test_save_location(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0) 

    #test delete
    def test_delete_image(self):
        self.new_location.save_location()
        location = Location.objects.filter(location='kimuhurura').first()
        delete = Location.objects.filter(location = location.location).delete()
        location = Location.objects.all()
        self.assertFalse(len(location)==1) 

    # Testing Update Method
    def test_update_image(self):  
        self.new_location.save_location()
        location = Location.objects.filter(location='kimuhurura').first()
        update = Location.objects.filter(location=location.location).update(location='gasabo')
        updated = Location.objects.filter(location='gasabo').first()
        self.assertNotEqual(location.location, updated.location)  

class CategoryTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.new_category = Category(category = "tourist")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))

    # Testing Save Method
    def test_save_category(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    #test delete
    def test_delete_image(self):
        self.new_category.save_category()
        category = Category.objects.filter(category='tourist').first()
        delete = Category.objects.filter(category = category.category).delete()
        category = Category.objects.all()
        self.assertFalse(len(category)==1) 

    # Testing Update Method
    def test_update_image(self):  
        self.new_category.save_category()
        category = Category.objects.filter(category='tourist').first()
        update = Category.objects.filter(category=category.category).update(category='animal')
        updated = Category.objects.filter(category='animal').first()
        self.assertNotEqual(category.category, updated.category)   
    
