from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)
    text = models.TextField(null=True)
    images = models.ImageField(null=True, blank=True, upload_to="website/templates/media/images/blog")
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + '|' + str(self.publish_date)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Podaj imię')
    content = models.TextField(verbose_name='Wpisz treść')
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.post.title) + '|' + self.name


# TODO change replay comments and all logic
class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, related_name="replays", on_delete=models.CASCADE)
    replay_name = models.CharField(max_length=100, verbose_name='Podaj imię')
    replay_content = models.TextField(verbose_name='Wpisz treść')
    replay_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment.post.title) + '|' + self.replay_name
