from rest_framework import serializers
from lib import constants as const
from apps.post.models import Post

class PostResponseSerializer(serializers.ModelSerializer):
	def to_representation(self, post):
		responseData = super().to_representation(post)
		if responseData[const.CATEGORY_PROPERTY]:
			category = responseData.pop(const.CATEGORY_PROPERTY)
			responseData[const.CATEGORY_PROPERTY] = \
				category[const.NAME_PROPERTY]
		if responseData[const.TAG_PROPERTY]:
			tags = responseData.pop(const.TAG_PROPERTY)
			responseData[const.TAG_PROPERTY] = \
				[tag[const.NAME_PROPERTY] for tag in tags]
		return responseData

	class Meta:
		model = Post
		fields = [
			const.ID_PROPERTY,
			const.TITLE_PROPERTY,
			const.DESCRIPTION_PROPERTY,
			const.CATEGORY_PROPERTY,
			const.TAG_PROPERTY,
			const.IMAGE_PROPERTY
		]
		depth = const.POST_RESPONSE_SERIALIZER_DEPTH
