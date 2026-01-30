from .models import News
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,address


class EditorRegistrationForm(UserCreationForm):
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    branch = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2','country','city','branch')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_editor = True
        if commit:
            user.save()
            country = self.cleaned_data.get('country')
            city = self.cleaned_data.get('city')
            branch = self.cleaned_data.get('branch')

            address.objects.create(
                country=country,
                city=city,
                branch=branch
                
            )
         
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })


class ViewerRegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_viewer = True
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })


# forms.py
class EditorLoginForm(AuthenticationForm):
    # Add any additional fields or customization for editor login form
    pass


class ViewerLoginForm(AuthenticationForm):
    # Add any additional fields or customization for viewer login form
    pass


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['category', 'Headline', 'image', 'Body']
