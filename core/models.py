from unicodedata import category
from django.db import models
from .commons import slugify

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField("Description")
    price = models.DecimalField("Price", max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.title)}-{self.id}'
        super(Product, self).save(*args, **kwargs)


class Filter(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='filters', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'

    def __str__(self):
        return f'{self.key} - {self.value}'


class Image(models.Model):
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name='images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.product.title


class Slider(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField("Description")
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['title']

    def __str__(self):
        return self.title


class AboutUS(models.Model):
    text = models.TextField('Text')

    class Meta:
        verbose_name = 'AboutUS'
        verbose_name_plural = 'AboutUS Texts'


class Shipping(models.Model):
    text = models.TextField('Text')

    class Meta:
        verbose_name = 'Shipping Text'
        verbose_name_plural = 'Shipping Texts'


class FAQ(models.Model):
    question = models.CharField(max_length=200, unique=True)
    answer = models.TextField('Text')
    # category = models.ForeignKey('FAQCategory', on_delete=models.CASCADE, db_index=True, related_name='faqs', null=True, blank=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class Order(models.Model):
    full_name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField(('email adress'),null=True, blank=True)
    address = models.CharField(max_length=5000)
    price = models.DecimalField("Price", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'