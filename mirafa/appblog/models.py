from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


CHOICE = (
    ('SOLVED', 'SOLVED'),
    ('INSTOCK', 'INSTOCK')
)
CATEGORY = (
    ('Science fiction','Science fiction'),
    ('Drama','Drama'),
    ('Romance','Romance'),
    ('Horror','Horror')
)


class Book(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField()
    category_books = models.CharField(
        max_length=40,
        choices=CATEGORY, default='Drama'
    )
    book_no = models.IntegerField(blank=True)
    status = models.CharField(
        max_length=40,
        choices=CHOICE, default='INSTOCK'
    )
    updated = models.DateTimeField(default=timezone.now)

    # def save(self, *args, **kwargs):
    #     ticket_id = Ticket.objects.count()
    #     if ticket_id == 0:
    #         self.ticket_id = 1
    #     else:
    #         self.ticket_id = ticket_id + 1
    #     return super(Ticket, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class BookComment(models.Model):

    book_comment = models.ForeignKey(Book, null=True, blank=True)
    person_name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        def __str__(self):
            return self.name
