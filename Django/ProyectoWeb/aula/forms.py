from django import forms
from .models import Cliente, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "edad", "direccion", "telefono"]
        widgets = {"email": forms.EmailInput(attrs={"autocomplete": "email"})}

    def clean_nombre(self):
        valor = self.cleaned_data["nombre"].strip()
        if not valor:
            raise forms.ValidationError("Ingresá un nombre.")
        return valor


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["numero", "cliente", "fecha", "entregado"]
        widgets = {"fecha": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"})}


class ContactoForm(forms.Form):
    asunto = forms.CharField(max_length=120)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={"rows": 5}))
