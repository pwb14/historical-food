import json

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from six import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
    """Author."""

    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    death_date = models.DateField()
    place_of_birth = models.CharField(max_length=16)

    class Meta(object):
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Simple tag model."""

    title = models.CharField(max_length=255)

    class Meta(object):
        """Meta options."""

        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipe")

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Book(models.Model):
    """Book."""

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField('recipes.Author', related_name='books')
    publication_date = models.DateField()
    pages = models.PositiveIntegerField(default=200)
    recipes = models.ManyToManyField('recipes.Recipe',
                                  related_name='books',
                                  blank=True)

    class Meta(object):
        """Meta options."""

        ordering = ["title"]

    def __str__(self):
        return self.title

    # As of tags, again, we only need a flat list of tag names, on which
    # we can filter. Therefore, we define a property on a model level,
    # which will return a JSON dumped list of tags relevant to the
    # current book model object.
    @property
    def tags_indexing(self):
        """Tags for indexing.

        Used in Elasticsearch indexing.
        """
        return [recipe.title for recipe in self.recipes.all()]