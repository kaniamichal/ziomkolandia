from django.db import models


class Join(models.Model):
    newsletter_email = models.EmailField()
    newsletter_timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.email

