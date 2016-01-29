from __future__ import unicode_literals

from django.db import models

# Create your fields here.

class TinyTextField(models.TextField):
	def db_type(self, connection):
		return 'tinytext'

class MediumTextField(models.TextField):
	def db_type(self, connection):
		return 'mediumtext'

class LongTextField(models.TextField):
	def db_type(self, connection):
		return 'longtext'

# Create your models here.

class Genre(models.Model):
	genre = models.TextField()

	def __str__(self):
		return self.genre

class Movie(models.Model):
	title = TinyTextField()
	description = models.TextField(blank=True)
	lens_id = models.IntegerField(blank=True,null=True)
	imdb_id = models.IntegerField(blank=True,null=True)
	tmdb_id = models.IntegerField(blank=True,null=True)
	link = models.URLField(blank=True)
	trailer = models.URLField(blank=True)
	genres = models.ManyToManyField(Genre,through='MovieGenres')

	def __str__(self):
		return self.title

class MovieGenres(models.Model):
	movie = models.ForeignKey(Movie)
	genre = models.ForeignKey(Genre)

	class Meta:
		auto_created = True
		ordering = ['genre',]

class Quiz(models.Model):
	TYPE_CHOICES = (
		('land','Landing Quiz'),
		('set','Quiz Set'),
	)

	quiz_type = TinyTextField(choices=TYPE_CHOICES)
	content = models.TextField()

	def __str__(self):
		return self.content

class QuizSet(models.Model):
	quiz = models.ForeignKey(Quiz)
	seq = models.IntegerField()
	content = models.TextField()

class Answer(models.Model):
	quiz = models.ForeignKey(Quiz)
	answer = TinyTextField()
	follow_quiz = models.ForeignKey(Quiz,related_name='follow_quiz')
	recommend_movie = models.ManyToManyField(Movie,through='RecommendMovie')

class RecommendMovie(models.Model):
	answer = models.ForeignKey(Answer)
	movie = models.ForeignKey(Movie)


