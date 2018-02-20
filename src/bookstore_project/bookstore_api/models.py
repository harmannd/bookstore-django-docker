from django.db import models

class Book(models.Model):
    EBOOK = 'EB'
    AUDIO = 'AU'
    NEWSPAPER = 'NP'
    FILE_TYPES = (
        (EBOOK, 'eBook'),
        (AUDIO, 'Audio'),
        (NEWSPAPER, 'Newspaper'),
    )
    ENGLISH = 'EN'
    SPANISH = 'SP'
    JAPANESE = 'JP'
    LANGUAGES = (
        (ENGLISH, 'English'),
        (SPANISH, 'Spanish'),
        (JAPANESE, 'Japanese'),
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_date = models.DateField()
    file_type = models.CharField(max_length=2, choices=FILE_TYPES, default=EBOOK)
    language = models.CharField(max_length=2, choices=LANGUAGES, default=ENGLISH)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


