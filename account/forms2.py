from django import forms
from django.contrib.auth.models import User

#UserModel = get_user_model()


class profileform(forms.ModelForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']



class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password']



    # username = forms.CharField(max_length=20)
    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    # email = forms.EmailField(max_length=30)
    # password1 = forms.PasswordInput()
    # password2 = forms.PasswordInput()
    