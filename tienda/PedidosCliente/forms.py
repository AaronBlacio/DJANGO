from django import forms

class Contactanos(forms.Form):
    asunto = forms.CharField()
    destinatario = forms.EmailField()
    mensaje = forms.CharField()