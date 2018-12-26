# Create your views here.

from .models import Product, ProductImage
from .serializers import ProductImageSerializer, ProductSerializer
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, ListView, \
    TemplateView, UpdateView
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView


class Home(TemplateView):
    template_name = "home.html"

############# AUTH ###################

class SignUp(TemplateView):
    template_name = "auth/signup.html"

class LogIn(TemplateView):
    template_name = "auth/login.html"
        
@method_decorator(login_required, name="dispatch")
class LogOut(TemplateView):
    template_name = "auth/logout.html"
    

######################################    
############## Manager ###############
######################################

############## Products ##############

@method_decorator(staff_member_required, name='dispatch')
class ProductList(ListView):
    model = Product
    template_name = 'manager/products/product_list.html'

@method_decorator(staff_member_required, name='dispatch')
class ProductDetail(DetailView):
    model = Product
    template_name = 'manager/products/product_detail.html'
    
@method_decorator(staff_member_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    fields = ['title','description','cost','stock']
    template_name = 'manager/products/product_create.html'    

@method_decorator(staff_member_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    fields = ['title','description','cost','stock']
    template_name = 'manager/products/product_update.html'    

@method_decorator(staff_member_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    template_name = 'manager/products/product_delete.html'   

################# Images #################

@method_decorator(staff_member_required, name='dispatch')
class ProductImageList(ListView):
    model = ProductImage
    template_name = 'manager/images/product_image_list.html'

@method_decorator(staff_member_required, name='dispatch')
class ProductImageDetail(DetailView):
    model = ProductImage
    template_name = 'manager/images/product_image_detail.html'

@method_decorator(staff_member_required, name='dispatch')
class ProductImageCreate(CreateView):
    model = ProductImage
    fields = ['caption','product','figure']
    template_name = 'manager/images/product_image_create.html' 

@method_decorator(staff_member_required, name='dispatch')
class ProductImageUpdate(UpdateView):
    model = ProductImage
    fields = ['caption','product','figure']
    template_name = 'manager/images/product_image_update.html' 

@method_decorator(staff_member_required, name='dispatch')
class ProductImageDelete(DeleteView):
    model = ProductImage
    fields = ['caption','product','figure']
    template_name = 'manager/images/product_image_delete.html' 


####################################################
###################### API #########################
####################################################

############## Product ##############

class APIProductCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()

class APIProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

############## ProductImage ##############

class APIProductImageCreateView(ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class APIProductImageDetailView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer