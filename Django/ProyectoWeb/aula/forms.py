from django import forms
from .models import Cliente, Pedido


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "email", "edad"]
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
