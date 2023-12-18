from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta :
        model = Listing  
        fields = ['title', 'price','num_bathroom','num_bedroom','square_footage','address',]