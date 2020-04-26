from django import forms
import re
from django.contrib.auth.models import User
from home.models import MyUser,code
class EditCode(forms.Form):
    codeedit=forms.CharField(widget=forms.Textarea)
    title=forms.CharField(max_length=200)
    img=forms.ImageField()
    def savecode_hasImg(self,nick):
        codea=code()
        codea.Code=self.cleaned_data['codeedit']
        codea.Title=self.cleaned_data['title']
        codea.Img=self.cleaned_data['img']
        codea.User=nick
        codea.save()
    def savecode_noImg(self,nick):
        codea=code()
        codea.Code=self.cleaned_data['codeedit']
        codea.Title=self.cleaned_data['title']
        codea.User=nick
        codea.save()

class EditProfile(forms.Form):
    firstname=forms.CharField(label="Họ",max_length=100)
    lastname=forms.CharField(label="Tên",max_length=100)
    namsinh=forms.IntegerField(label="Năm sinh")
    uid=forms.IntegerField(label="uid")
    noio=forms.CharField(label="Nơi ở",max_length=200)
    def edit_OK(self,nick):
        username=MyUser.objects.get(username=nick)
        username.first_name=self.cleaned_data['firstname']
        username.Noio=self.cleaned_data['noio']
        username.last_name=self.cleaned_data['lastname']
        username.Namsinh=self.cleaned_data['namsinh']
        username.Uid=self.cleaned_data['uid']
        username.save()

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
