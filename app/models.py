from django.db import models


class PostData(models.Model):
    '''
    its a simple database that consist of name email and ICO field
    in django admin site ico data will be visible at front
    '''
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default=None)
    ico = models.CharField(max_length=8)

    def __str__(self):
        return self.ico
   