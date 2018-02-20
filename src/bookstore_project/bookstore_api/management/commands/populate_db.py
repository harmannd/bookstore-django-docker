from django.core.management.base import BaseCommand
from bookstore_api.models import Book

from datetime import date
from random import choice, randint
from string import capwords

class Command(BaseCommand):
    help = 'Used to populate the database with dummy objects'
    words = [
        'people', 'history', 'way', 'art', 'world', 'information',
        'map', 'two', 'family', 'government', 'health', 'system',
        'computer', 'meat', 'year', 'thanks', 'music', 'person',
        'reading', 'method', 'data', 'food', 'understanding', 'theory',
        'law', 'bird', 'literature', 'problem', 'software', 'control',
        'knowledge', 'power', 'ability', 'economics', 'love', 'internet',
        'television', 'science', 'library', 'nature', 'fact',
        'product', 'idea', 'temperature', 'investment', 'area',
        'society', 'activity', 'story', 'industry', 'media', 'thing',
        'oven', 'community', 'definition', 'safety', 'quality',
        'development', 'language', 'management', 'player', 'variety'
    ]
    names = [
        'John', 'Jeff', 'Amy', 'Bill', 'Derek', 'Jessica',
        'Johnson', 'Smith', 'Betsy', 'Jim', 'Ben', 'Lori',
        'Zach', 'Courtney', 'Alice', 'Anderson', 'Alex',
        'Will', 'James', 'Ethan', 'Mason', 'Noah', 'Nate',
        'Ryan', 'Hunter', 'Levi', 'Caleb', 'Owen', 'Alexis',
        'Alison', 'Vickie', 'Valery', 'Victoria'
    ]
    text = "Lorem Ipsum is simply dummy text of the printing" \
        + "and typesetting industry. Lorem Ipsum has been the " \
        + "industry's standard dummy text ever since the 1500s, " \
        + "when an unknown printer took a galley of type and " \
        + "scrambled it to make a type specimen book. It has " \
        + "survived not only five centuries, but also the leap " \
        + "into electronic typesetting, remaining essentially " \
        + "unchanged."

    def _create_books(self):
        for x in range(0, 100):
            book = Book(
                title=self.getTitle(),
                author=self.getName(),
                pub_date=date(randint(1800, 2017), randint(1, 12), randint(1, 28)),
                file_type=choice(Book.FILE_TYPES)[0],
                language=choice(Book.LANGUAGES)[0],
                summary=self.text
            )
            book.save()

    def getTitle(self):
        title = ""
        for x in range(0, randint(1, 4)):
            title += choice(self.words) + " "
        return capwords(title[:-1])

    def getName(self):
        return choice(self.names) + " " + choice(self.names)

    def handle(self, *args, **options):
        self._create_books()