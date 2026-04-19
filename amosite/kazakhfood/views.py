from .models import ContactMessage
from django.shortcuts import render, get_object_or_404
from .models import Dish, Category
from .forms import BookingForm
from .models import BlogPost


def index(request):
    return render(request, 'kazakhfood/index.html')


def about(request):
    return render(request, 'kazakhfood/about.html')

def delivery(request):
    return render(request, 'kazakhfood/delivery.html')


def menu(request, category_slug=None):
    categories = Category.objects.all()
    dishes = Dish.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        dishes = dishes.filter(category=category)

    return render(request, 'kazakhfood/menu.html', {
        'categories': categories,
        'dishes': dishes
    })


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'kazakhfood/dish_detail.html', {
        'dish': dish
    })


def blog(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'kazakhfood/blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, is_published=True)
    return render(request, 'kazakhfood/blog_detail.html', {'post': post})


def reserve(request):
    success = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = BookingForm()
    else:
        form = BookingForm()
    return render(request, 'kazakhfood/reserve.html', {'form': form, 'success': success})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "kazakhfood/contacts.html", {
            "success": True
        })

    return render(request, "kazakhfood/contacts.html")