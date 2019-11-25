from rest_framework import serializers

from eNumber.models import eNumber

class eNumberSerializer(serializers.ModelSerializer): #Forms.ModelForm
	class Meta:
		model = eNumber
		fields = [
			'number',
			'name',
			'description',
			'status',
		]