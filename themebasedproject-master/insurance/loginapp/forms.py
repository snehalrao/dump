from django import forms
from loginapp.models import User_insurance

class Insuranceform(forms.ModelForm):
    class Meta:
        # model is a keyword
        # or else it will throw value error

        model = User_insurance
        fields = '__all__'
        #for labels

        labels = {
            'usr_id' : 'Username',
            'usr_pass' : 'Password'
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
