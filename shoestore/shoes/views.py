from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, render,redirect
from .models import ShoeModel,Order,Cart
from django.views.generic import ListView,DetailView,FormView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

# Create your views here.

"""authentication"""
class CustomLoginView(LoginView):
    template_name ='login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) :
        return reverse_lazy('shoeslist')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('shoeslist')

    def form_valid(self, form):
        user = form.save()
        if self.request.method == "POST":
            if user is not None:
                login(self.request, user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('shoeslist')
        return super(RegisterPage,self).get(*args,**kwargs)
    
def home(request):
    return render(request,'index.html')
    


"""user_functions"""


class ShoeListView(ListView):
    model = ShoeModel
    template_name = 'shoelist.html'

class ShoeDetailView(DetailView):
    model = ShoeModel
    fields = '__all__'
    template_name = 'shoedetail.html'


class ShoeCheckoutView(DetailView):
    model = ShoeModel
    template_name = 'checkout.html'

def BuyShoeView(request,pk):
    product = ShoeModel.objects.get(id=pk)
    Order.objects.create(user = request.user,product=product)
    return render (request,'order.html')


class ShoeOrderView(ListView):
    model = Order
    template_name = 'orderlist.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user = self.request.user)
        return context

def add_to_order(request, pk):
    Product = get_object_or_404(ShoeModel, pk=pk)
    order_item,created = Order.objects.get_or_create(
        user=request.user,
        product= Product,
    )
    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect('orderlist')



"""Cart"""

def add_to_cart(request, pk):
    Product = get_object_or_404(ShoeModel, pk=pk)
    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        product= Product,
        price=Product.price,
        image_url = Product.image_url,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


# class ViewCart(ListView):
#     model = Cartmodel
#     template_name = 'viewcart.html'
#     context_object_name = 'products'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products']= context['products'].filter(user = self.request.user)
#         return context

# def AddtoCart(request,pk):
#     context={}
#     product = ShoeModel.objects.get(id=pk)
#     cart_products=Cart.objects.filter(product__name =product)
#     # if product in cart_products:
#     #     context['message'] = "In cart"
#     # else:
#     #     context['message'] = "new"
#     Cartmodel.objects.create(user=request.user,product=product)

#     context['product']=product
#     context['cart'] = cart_products
        
    
#     return render (request,'cart_add.html',context)

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'cartitemdelete.html'
    success_url = reverse_lazy('cart')


def orderfromcart(request,pk):
    context={}
    
    return render(request,'order.html',context)


"""wishlist"""


"""search"""
class SearchResultsView(ListView):
    model = ShoeModel
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return ShoeModel.objects.filter(Q(name=query) | Q(name=query))
    


    











































# def PaymentComplete(request):
#     body=json.loads(request.body)
#     print('BODY:',body)
#     product=Book.objects.get(id=body['prosuctId'])
#     Order.objects.create(product=product)
#     return JsonResponse('Payment completed',safe=False)







# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         myuser = User.objects.create_user(username, email, pass1)

#         myuser.save()

#         return redirect('signin')

#     return render(request, 'signup.html')


# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             fname = user.username
#             return render(request, 'shoelist.html', {'fname': fname})

#         else:
#             return redirect('signin')

#     return render(request, 'signin.html')


# def signout(request):
#     logout(request)
#     messages.success(request, 'Logged out Successfully!')
#     return redirect('signin')


