# We maintain the models we define in a seperate file called models.py.
# Think of models as spread sheets with columns. Here is the file where
# we deine the columns. (The objects in OOPs).

from django.conf import settings
# To maintain a lighter app we only import modules we need.
# from is the name of the module and import makes us import only a specific part.
from django.db import models
from django.utils import timezone


# class defines an Object. Post is the name of the object. And models.Model means it's a model.
# Let the confusing name not get you :P.
class Post(models.Model):
# Fields of our model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link to another model
    title = models.CharField(max_length=200) # define char with spefic length
    text = models.TextField() # define long text without a limit.
    created_date = models.DateTimeField(default=timezone.now) # define date and time. use the timezone from settings.py
    published_date = models.DateTimeField(blank=True, null=True) # Specify publish date with blank and null true.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# We can change the name of methods but use lowercases and underscores instead of spaces.
# Please indent code. Otherwise methods wont belong to the same class.
# Explain the keyword self. The method publish takes in a self object and sets the timezone to present time.
# the method __str__ returns a string called title defined on the object POST.
# Add some brainstorming activity and hands on here.
