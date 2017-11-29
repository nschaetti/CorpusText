# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# A text
class Text(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publishing date")

    def __str__(self):
        return self.title
    # end __str__
# end Text


# An author
class Author(models.Model):

    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Text, through='Authorship')

    def __str__(self):
        return self.name
    # end __str__

# end Author


# An authorship
class Authorship(models.Model):

    text = models.ForeignKey(Text)
    author = models.ForeignKey(Author)

    def __str__(self):
        return "{0} written by {1}".format(self.text, self.author)
    # end __str__

# end Authorship
