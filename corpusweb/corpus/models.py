# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# A country
class Country(models.Model):
    """
    A country
    """

    # Properties
    name = models.CharField(max_length=100)

# end Country


# A genre
class Genre(models.Model):
    """
    A Sci-Fi genre
    """

    # Properties
    name = models.CharField(max_length=100)

# end Genre


# A text
class Text(models.Model):
    """
    A text document
    """

    # Properties
    average_rating = models.FloatField()
    classes = models.ForeignKey(Class)
    content = models.TextField(null=True)
    copyright = models.TextField(null=True)
    cover = models.ImageField()
    description = models.TextField(null=True)
    goodreads = models.CharField(max_length=200)
    gutenberg = models.CharField(max_length=200)
    gutenberg_num = models.IntegerField()
    isbn = models.CharField(max_length=13)
    language = models.SmallIntegerField(choices=((0, 'English'), (1, 'French'), (2, 'Dutch')))
    loc_class = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    pages = models.IntegerField()
    plot = models.TextField(null=True)
    publishing_date = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name="Publishing date")
    rating_count = models.IntegerField()
    summary = models.TextField(null=True)
    title = models.CharField(max_length=100)
    type = models.SmallIntegerField(choices=((0, 'Novel'), (1, 'Short Story'), (2, 'Novella')))
    wikipedia = models.CharField(max_length=200)
    year = models.IntegerField()

    # To string
    def __str__(self):
        """
        To string
        :return:
        """
        return "{} ({})".format(self.title, self.publishing_date)
    # end __str__

# end Text


# A person (author, translator, publisher)
class Person(models.Model):
    """
    A person (author, translator, publisher
    """
    # Properties
    #books = models.ManyToManyField(Text, through='Authorship')
    born = models.DateField(null=True)
    bio = models.TextField(null=True)
    died = models.DateField(null=True)
    gender = models.PositiveSmallIntegerField(choices=((0, 'Male'), (1, 'Female')))
    name = models.CharField(max_length=30)
    summary = models.TextField(null=True)
    wikipedia = models.CharField(max_length=100)

    # To string
    def __str__(self):
        """
        To string
        :return:
        """
        return "{} ({} - {})".format(self.name, self.born, self.died)
    # end __str__

    # To unicode
    def __unicode__(self):
        """
        To unicode
        :return:
        """
        return u"{} ({} - {})".format(self.name, self.born, self.died)
    # end __unicode__

# end Person


# An authorship
class Authorship(models.Model):

    text = models.ForeignKey(Text)
    author = models.ForeignKey(Author)

    def __str__(self):
        return "{0} written by {1}".format(self.text, self.author)
    # end __str__

# end Authorship
