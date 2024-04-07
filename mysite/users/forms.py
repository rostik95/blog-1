from django import forms
from django.contrib.auth import get_user_model


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        labels = {'email': 'Адрес электронной почты',
                  'first_name': 'Имя',
                  'last_name': 'Фамилия'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким username уже существует')
        return username
