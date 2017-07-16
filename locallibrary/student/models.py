from django.db import models
import uuid # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower

# Create your models here.
class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    id = models.CharField(primary_key=True, max_length=50, help_text="Unique ID for this particular book across whole library")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        
       

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
        

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        permissions = (("can_mark_returned", "Set book as returned"),)   

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s (%s)' % (self.id,self.book.title)