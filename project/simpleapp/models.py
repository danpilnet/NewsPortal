
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    rating = models.IntegerField(default = 0)

    def uptade_rating(self):
        posts_rating = self.post_set.aggregate(pr=Coalesce(Sum('rating_post'), 0)).get('pr')
        comments_rating = self.user.comment_set.aggregate(cr=Coalesce(Sum('rating_comment'), 0)).get('cr')
        posts_comments_raring = self.post_set.aggregate(pcr=Coalesce(Sum('rating_post'), 0)).get('pcr')

        self.rating = posts_rating * 3 + comments_rating + posts_comments_raring
        self.save()

    def __str__(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Post(models.Model):

    article = 'AR'
    news = 'NE'

    POSITION = [(article, 'Статья'),
                (news, 'Новости')]


    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_news = models.CharField(max_length=2,choices=POSITION,default=news)
    post_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category,through='PostCategory')
    post = models.CharField(max_length=200)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)


    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return f"{self.text[:124]}..."


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})





class PostCategory(models.Model):
    post_ps = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_ct = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)


    def like(self):
        self.rating_comment += 1
        self.save()


    def dislike(self):
        self.rating_comment -= 1
        self.save()