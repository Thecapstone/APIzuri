from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.identifier = slugify(self.description)
        super().save(*args, **kwargs)
        pass

    def get_absolute_url(self):
        return reverse("links_detail", kwargs={"identifier": self.identifier})
