from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Armada, Testi, Order


class ArmadaForm(ModelForm):
    class Meta:
        models = Armada
        fields = '__all__'


class TestiForm(ModelForm):
    class Meta:
        model = Testi
        fields = '__all__'


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['armada'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['tgl_mulai'].widget.attrs.update({'class': 'form-control w-75', 'placeholder': 'yyyy-mm-dd'})
        self.fields['durasi'].widget.attrs.update({'class': 'form-control w-75'})

        

    class Meta:
        model = Order
        exclude = ['user', 'status']

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']