from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
	#By using model serializer we can actually concise and less replicating

	class Meta:
		model=Snippet
		fields=('id','title','code','linenos','language','style')
"""
class SnippetSerializer(serializers.Serializer):
	pk=serializers.IntegerField(read_only=True)
	title=serializers.CharField(required=False, allow_blank=True, max_length=100)
	code=serializers.CharField(style={'base_template':'textarea.html'})
	linenos=serializers.BooleanField(required=False)
	language=serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style=serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

	def create(self, validated_data):
		
		#This functions creates a Snippet instance of the given validated data and saves it in database
		
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		
		#To update the selected instance on db
		
		instance.title=validated_data.get('title', instance.title)
		instance.code=validated_data.get('code',instance.code)
		instance.linenos=validated_data('linenos',instance.linenos)
		instance.language=validated_data('language',instance.language)
		instance.style=validated_data('style',instance.style)
		instance.save()
		return instance
"""