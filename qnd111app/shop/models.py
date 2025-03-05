from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(max_length=200,
                            db_index=True),
    slug = models.SlugField(max_length=200,
                            unique=True),

    image = models.ImageField(upload_to='categories/%Y/%m/%d',
                              blank=True),
    salidas = models.DateTimeField(null=True),
    desde =  models.CharField(max_length=200, null=True),
    description = models.TextField(blank=True,null=True),
    detail = models.FileField(upload_to='tours/%Y/%m/%d',null=True),
    terms = models.TextField(blank=True),

    )

    class Meta:
        #ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields( 
    
    name = models.CharField(max_length=200, db_index=True),
    slug = models.SlugField(max_length=200, db_index=True),
    description = models.TextField(blank=True),
    price = models.DecimalField(max_digits=10, decimal_places=2),
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,null=True),
    
    )
    available = models.BooleanField(default=True)

    item1 = models.CharField(max_length=200,null=True)
    item2 = models.CharField(max_length=200,null=True)
    item3 = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    #class Meta:
     #   ordering = ('name',)
     #   index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail',
                           args=[self.id, self.slug])
