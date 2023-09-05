from django.db import models

class Announcement(models.Model):
    
    LEARN = "Хочу научиться"
    TEACH = "Могу научить"
    TYPE_OF_ADS = [
        (LEARN,"Хочу научиться"),
        (TEACH,"Могу научить"),
    ]
    
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name='announcement', null=True, blank=True)
    title = models.CharField(max_length=155, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    type = models.CharField(max_length=100,choices=TYPE_OF_ADS, default=LEARN)
    main_image = models.ImageField(upload_to="images/announcement/", blank=True, verbose_name='фото')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='announcement', null=True, blank=True)
    
    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Обьявлении'
        verbose_name_plural = 'Обьявления'
        
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.title


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
    
    def __str__(self):
        return self.title

    
