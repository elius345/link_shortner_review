from django.db import models
import random
import string
from django.db import IntegrityError
def code_generator():
    letters = string.ascii_letters
    digits = string.digits
    character = letters+digits
    sample_char = ''.join(random.sample(character, 5))
    return sample_char

# Create your models here.
class LinkShortener(models.Model):
    long_url = models.CharField(max_length=250, unique=True)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.long_url

    def save(self, *arg, **kwarg):
        if not self.code:
            while True:
                try:
                    self.code = code_generator()
                except IntegrityError:
                    continue
                break
        return super().save(*arg, **kwarg)



