from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.


def İndex(request):

    product = Product.objects.all()
    categori = Categories.objects.all()
    
    query=request.GET.get('q')
    if query:
        product=product.filter(
            Q(title__icontains=query)|
            Q(product_detail__icontains=query)|
            Q(category__title__icontains=query)|
            Q(product_price__icontains=query)
            
        ).distinct

    context = {
        "product": product,
        "categori": categori

    }

    return render(request, 'index.html', context)


def Category(request, id):
    product = Product.objects.filter(category=id)
    categori = Categories.objects.all()

    context = {
        "product": product,
        "categori": categori,
    }

    return render(request, 'categories.html', context)


def Detail(request, id):
    product = Product.objects.get(id=id)
    categori = Categories.objects.all()
    comment = Comment.objects.filter(product_comment=product)

            
    if request.method == 'POST':
        comment = request.POST['comments']
        comm = Comment(comments=comment, product_comment=product)
        comm.save()

        return redirect('/detay/'+id+'/')
    
    

    context = {
        "product": product,
        "categori ": categori,
        "comment": comment
    }

    return render(request, 'detail.html', context)



def Register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=firstname).exists():
                context = {
                    "information": "Bu kullanıcı kullanılıyor, farklı bir kullanıcı adı deneyiniz."
                }
                return render(request, 'register.html', context)

            if User.objects.filter(email=email).exists():

                context = {
                    "information": "E-mail adresi kullanılıyor farklı bir mail ile kayıt işlemine devam edebilirsiniz."
                    
                }
                return render (request,'register.html',context)
            
            else:
                user=User.objects.create_user(username=firstname, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                
                return redirect("kaydol")

        else:
            context = {
                "information": "Parolanız girmiş olduğunuz parolayla uyuşmuyor, kontrol ediniz."
            }

            return render(request, 'users/register.html', context)

    return render(request, 'users/register.html')

def Login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('Anasayfa')
        else:
            
            context={
                "information":"Hatalı kullanıcı adı veya parola girdiniz."
            }
            return render(request,'users/login.html',context)
        
    return render(request,'users/login.html')


def Logout(request):
    
    logout(request)
    return redirect('giris')


@login_required(login_url='/giris/')
def Profil(request):
    categories=Categories.objects.all()

    if request.method=="POST" and "user" in request.POST:
        user=request.user
        user.username = request.POST['username']
        user.first_name =request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        
    
    if request.method =="POST" and "product" in request.POST:
        title=request.POST['product_name']
        product_detail=request.POST['product_title']
        product_price=request.POST['product_price']
        product_img = request.FILES['product_img']
        category_id =request.POST['category']
        
        category=Categories.objects.get(id=category_id)
        
        product=Product(title=title,product_detail=product_detail,product_price=product_price,product_img=product_img,category=category)
        product.save()

        return redirect('Anasayfa')
    
    
    context={
        "categories":categories
    }
    

    return render(request,'profil.html',context)

def ürünEkle(request,product_id):
    product=Product.objects.get(id=product_id)
    user=request.user
    sepet=Sepet.objects.create(user=user,Product=product,adet=1, allprice=product.product_price)
    sepet.save()
    
    return redirect('sepet')


def Shopping(request):
    sepet= Sepet.objects.filter(user=request.user)
    
    context={
        "sepet":sepet
    }
    
    return render(request,'shop.html',context)