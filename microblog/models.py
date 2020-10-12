from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation

from star_ratings.models import Rating
# from users.models import Users


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    id_author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, verbose_name='Autor')
    category = models.ManyToManyField(BlogCategory, verbose_name='Kategorie', blank=True)
    tag = models.CharField('Tagi', max_length=50, blank=True)
    title = models.CharField('Tytuł', max_length=100)
    short = models.TextField('Skrót', max_length=1000)
    contents = RichTextField('Pełna treść', max_length=100000000, blank=True, null=True)
    created_date = models.DateTimeField('Data utworzenia', default=timezone.now)
    publication_date = models.DateTimeField('Data publikacji', blank=True, null=True)
    rating = GenericRelation(Rating, related_query_name="posts")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"

    def __str__(self):
        return self.title

    def get_avg_rating(self):
        if self.rating.exists():
            return f'średnia ocen: {(round(float(self.rating.get().average), 2))}'
        else:
            return "brak ocen"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    name = models.CharField('Autor', max_length=80, default='Anonim')
    text = models.TextField('Treść', max_length=500)
    email = models.EmailField('Email', blank=True)
    created = models.DateTimeField('Data utworzenia', auto_now_add=True)
    update = models.DateTimeField('Data modyfikacji', blank=True, null=True)
    active = models.BooleanField('Aktywny', default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

    def __str__(self):
        return 'Komentarz utworzony przez {} do wpisu {}'.format(self.name, self.post)
