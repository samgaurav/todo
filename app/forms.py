from django.forms import ModelForm
from . models import TODO
#What is ModelForm Django?
'''Image result for Modelform django
Django ModelForm is a class that is used to directly convert a model into a Django form
'''
class TODOForm(ModelForm):

    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority' ] #that three fields we are using
