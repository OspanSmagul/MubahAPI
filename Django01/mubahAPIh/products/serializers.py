from rest_framework import serializers

from products.models import Products

class ProductsSerializer(serializers.ModelSerializer): #Forms.ModelForm
	class Meta:
		model = Products
		fields = [
			'pk',
			'barcode',
			'name',
			'ingridients',
			'status',
			'why_haram',
			'why_doubtful',
		]


