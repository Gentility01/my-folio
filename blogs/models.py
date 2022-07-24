from django.db import models
from home.models import Userprofile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
        
class Folio_Blog(models.Model):
    title = models.CharField( max_length=50)
    blog_tags = models.CharField( max_length=50)
    image = models.ImageField( upload_to="images")
    description    = RichTextField()
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE) 
    datecreated = models.DateTimeField( auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Folio_Blogs'
        
# class RecentPages(models.Model):
#     title = models.ForeignKey(Folio_Blog, on_delete=models.CASCADE) 
    
    
class Comments(models.Model):
    blog_comment =  models.ForeignKey(Folio_Blog,related_name='comments', on_delete=models.CASCADE)
    commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_added = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f'{self.commenter_name.username} comment  :{self.comment_body} '
    
    class Meta:
        verbose_name_plural = 'Comments'
        
# class ReplyingComent(models.Model):
#     comment_on =  models.ForeignKey(Comments, related_name='r_comments', on_delete=models.CASCADE)
#     r_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     comment_body = models.CharField( max_length=500)
#     date_added = models.DateTimeField( auto_now_add=True)
    
#     def __str__(self):
#         return f'{self.r_name.username} replyed :{self.comment_on} '
    
