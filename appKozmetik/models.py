from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Categories(models.Model):
    title=models.CharField(("Kategori adı"), max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(("Ürünün adı"), max_length=50)
    product_detail=models.TextField(("Ürünün açıklaması"),null=True,blank=True)
    product_price =models.IntegerField(("Ürünün fiyatı"),null=True,blank=True)
    product_img=models.ImageField(("Ürünün fotoğrafı"), upload_to=None,null=True,blank=True)
    category=models.ForeignKey(Categories, verbose_name=("categories"), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title

    
class Comment(models.Model):
    time=models.DateTimeField(("Saat"),default=timezone.now, auto_now=False, auto_now_add=False)
    comments=models.TextField(("Yorum"),null=True,blank=True)
    product_comment=models.ForeignKey(Product, verbose_name=(""), on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.product_comment
    
class Profil(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product= models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)

class Sepet(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    Product= models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    adet = models.IntegerField(("adet"), max_length=50,null=True,blank=True)
    allprice = models.FloatField(("Toplam Fiyat"))