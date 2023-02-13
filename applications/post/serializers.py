from rest_framework import serializers
from applications.post.models import Post, PostImage, Comment


class PostImagesSerializer(serializers.ModelSerializer):


    class Meta:
        model = PostImage
        fields = '__all__'
        # fields = ('id',)
        # exclude = ('post',)
        


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(required=False)
    images = PostImagesSerializer(many=True, read_only = True)
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

    def create(self, validate_data):
        post = Post.objects.create(**validate_data)

        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post, image=i)
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(PostImage(post=post, image=i))
        PostImage.objects.bulk_create(image_objects) # bulk_create он создает список обьектов добовляет одним запросом

        return post


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'        