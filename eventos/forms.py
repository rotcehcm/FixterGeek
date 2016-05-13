from django import forms
from .models import Aplicant
from django.utils.translation import ugettext_lazy as _


class AplicaForm(forms.ModelForm):

	class Meta:
		model = Aplicant
		fields = ['motivos','beca','tipo','porque']
		labels={
		'motivos':_('Dínos, ¿porqué quieres entrar a Fixter.Camp?'),
		'beca':_('¿Crees que necesitas una Beca?'),
		'porque':_('Explicanos porque necesitas la beca de descuento:')
		}
		widgets = {
            'beca': forms.RadioSelect(attrs={'class':'.beca'})
        }




		# 'email':_('Introduce tu correo electrónico')
		# }
		# widgets = {
		# 	'nombre':forms.TextInput(attrs={'class':'rellenito','placeholder':'Tu nombre mijo','id':'morro'}),
		# }