from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField('Название поста', max_length=50, null=True, blank=True)
    description = models.TextField('Описание поста')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='posts', 
        verbose_name='Владелец поста',
        )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

