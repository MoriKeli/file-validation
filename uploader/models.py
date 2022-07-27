from django.db import models

class UserFiles(models.Model):
    file_name = models.CharField(max_length=100)
    ufile = models.FileField(upload_to='Files/')
    uploaded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.file_name}'
    
    class Meta:
        verbose_name_plural = 'User Files'