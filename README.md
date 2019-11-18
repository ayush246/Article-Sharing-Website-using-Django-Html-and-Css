# Outlay and UI Design :

### Home page displaying all the features of the website

![1](https://user-images.githubusercontent.com/37112252/69032658-08615e80-0a03-11ea-8c62-5b1fe5e6e47b.png)



### SignUp and Login Pages for the creation and authentication of users

![2](https://user-images.githubusercontent.com/37112252/69032662-0b5c4f00-0a03-11ea-857d-cc9d8ac22cb8.png)

![3](https://user-images.githubusercontent.com/37112252/69032836-6e4de600-0a03-11ea-9345-49ff55fec700.png)



### Once logged in , the users can post a new article through this create post form

![4](https://user-images.githubusercontent.com/37112252/69032669-0e573f80-0a03-11ea-958a-a0db2c897a81.png)



### Users can review each article , see the ones they like in detail and upvote their favourite article
![6](https://user-images.githubusercontent.com/37112252/69032673-131bf380-0a03-11ea-97fa-781c51f251f5.png)
![5](https://user-images.githubusercontent.com/37112252/69032671-11523000-0a03-11ea-8b44-e1f5600adbd1.png)

# Code snippets :

### Authentication

```python
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
def sign_up(request):
    if request.method=="POST":
        #the user wants to sign up after entering their information
        if request.POST['password1']=="" or request.POST['username']=="":
            return render(request,"accounts/sign_up.html",{'error':"must enter all fields"})
        elif request.POST['password1']==request.POST['password2']: # everything used here is referenced in sign_up.html 
                                                                 # under the form tag and is called using name given
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,"accounts/sign_up.html",{'error':"username is already taken"})
            except User.DoesNotExist: # condition for if user doesn't exist and the passwords entered match
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,"accounts/sign_up.html",{'error':"passwords enter do not match"})
    else:
        #user wants to enter info
        return render(request,"accounts/sign_up.html")
def login(request):
    if request.method=="POST":
        print (request.body)
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,"accounts/login.html",{'error':"username or password incorrect"})
    else:
        return render(request,"accounts/login.html")
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
    return render(request,"accounts/sign_up.html")
```

### Navigation and Functioning

```python
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from django.utils import timezone

def landing(request):
    products = Article.objects
    return render(request,"products/landing.html",{'products':products})

def home(request):
    products = Product.objects
    return render(request,"products/home.html",{'products':products})

@login_required #if the user is not logged in and tries to access this page they are sent elsewhere

def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            # validating url by adding http://
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.votes_total = 1
            product.save()
            return redirect('/products/'+ str(product.id))
        else:
            return render(request,"products/create.html",{'error':'All fields are required'})
    else:
        return render(request,"products/create.html")

def detail(request,product_id):
    product = get_object_or_404(Article,pk=product_id)
    return render(request,"products/detail.html",{'product':product})

@login_required(login_url="/accounts/signup")

def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Article, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))

```
