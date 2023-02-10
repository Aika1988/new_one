from rest_framework import serializers
from applications.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(required=False)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta():
        model = Post
        # fields = ('title',)
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)   
    #     # print(representation)
    #     # representation['name'] = 'John' # можем таким образом переопеределить имя владельца
    #     representation['owner'] = instance.owner.email     # таким образом мы вытищили владельцев каждого поста
    #     return representation 


    # def create(self, validate_data):
    #     validate_data['owner'] = self.context['request'].user
    #     return super().create(validate_data)

