from django import forms
from .models import Subscriber

class SubcriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already subscribed.")
            return email
        

class NewsletterForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'rows': 5}))