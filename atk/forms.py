from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import Form, ModelForm, DateField, widgets


class loginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Username",
                "aria-label": "Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Password",
                "aria-label": "Password"
            }
        )
    )

class addUserForm(UserCreationForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Email",
                "aria-label": "Email"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Username",
                "aria-label": "Username"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Password",
                "aria-label": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Password",
                "aria-label": "Password"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name' , 'is_admin', 'is_pimpinanunit', 'is_wadir', 'is_adminunit')
        
class DateInput(forms.DateInput):
    input_type = 'date'
    
#WADIR
class formJadwal(forms.ModelForm):
    
    YEAR_CHOICES = []
    for r in range(2023, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))
    
    tahun = forms.ChoiceField(choices=YEAR_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Pilih ATK",

            }
        )
    )
    
    pengajuan_mulai = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "date"
            }
        )
    )
    
    pengajuan_selesai = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "date"
            }
        )
    )
    
    keterangan=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "text"
            }
        )
    )
    
    class Meta:
        model = Jadwal
        fields = '__all__'
        exclude = ['status']
        labels = {'tahun': 'Tahun', 
                  'pengajuan_mulai': 'Tanggal Dibuka',
                  'pengajuan_selesai': 'Tanggal Ditutup'
                }
        
class formPengumpulanPengajuan(forms.ModelForm):
    class Meta:
        model= pengumpulanPengajuan
        fields = '__all__'
        
class formIsiPengajuan(forms.ModelForm):
    atk = forms.ModelChoiceField(queryset=Barang_ATK.objects.all(), empty_label=None,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "placeholder": "Pilih ATK",

            }
        )
    )
    
    jumlah = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Jumlah",
                "min": 1,
            }
        )
    )
    keterangan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Keterangan",

            }
        )
    )
    
    
    class Meta:
        model = Isi_pengajuan
        fields = '__all__'
        exclude = ["rekomendasi", "pengajuan"]
        labels = {'atk': 'Pilih Barang', 
                  'jumlah': 'Jumlah Diajukan',
                  'keterangan': 'Keterangan'
                }

   