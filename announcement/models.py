from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    main_image = models.ImageField(upload_to="images/announcement/", blank=True, verbose_name='фото')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    
    class Meta:
        ordering = ('created_at',)
        
    def __str__(self) -> str:
        return self.title
    
        
    
