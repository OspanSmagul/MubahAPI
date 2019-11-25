from rest_framework import serializers

from companies.models import Company

class CompanySerializer(serializers.ModelSerializer): #Forms.ModelForm
	class Meta:
		model = Company
		fields = [
			'id',
			'company_name',
			'brand_name',
			'address',
			'email',
			'site',
			'contact',
			'logo',
			'chicken_status',
			'beaf_status',
			'mutton_status',
			'horsemeat_status',
		]