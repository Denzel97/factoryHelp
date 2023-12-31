from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Company(models.Model):
    page_name = models.CharField(max_length=255)
    logo_colour = models.CharField(max_length=255)
    logo_country_name = models.CharField(max_length=255)
    logo_country_flag = models.CharField(max_length=255)  # Assuming CharField for image URLs
    logo_image = models.CharField(max_length=255, null=True, blank=True, default='')

    def __str__(self):
        return self.page_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    short_description = models.TextField()
    description = models.TextField()
    image_url = models.URLField()
    images_gala = models.TextField()
    sku = models.CharField(max_length=255)
    downloadable_images = models.TextField()
    pdf_link = models.URLField()
    scraping_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
