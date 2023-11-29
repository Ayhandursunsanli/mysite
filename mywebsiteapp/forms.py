from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'Ad Soyad' ,widget=forms.TextInput(attrs={'placeholder': 'Ad Soyad'}))
    email = forms.EmailField(label= 'Email' ,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=200, label= 'Konu' ,widget=forms.TextInput(attrs={'placeholder': 'Konu'}))
    message = forms.CharField(widget=forms.Textarea, label='Mesaj')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email or '@' not in email:
    #         raise forms.ValidationError("Geçerli bir e-posta adresi girin.")
    #     return email