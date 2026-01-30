from django.shortcuts import render, redirect
from .models import MenuItem, ContactMessage, Order, OrderItem, Reservation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def menu(request):
    hot = MenuItem.objects.filter(category='hot')
    cold = MenuItem.objects.filter(category='cold')
    snacks = MenuItem.objects.filter(category='snacks')
    dessert = MenuItem.objects.filter(category='dessert')

    return render(request, 'menu.html', {
        'hot': hot,
        'cold': cold,
        'snacks': snacks,
        'dessert': dessert
    })


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')



@login_required(login_url='/login/')
def add_to_cart(request, item_id):
    if request.method == "POST":
        order_id = request.session.get('order_id')

        if not order_id:
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=request.user.username if request.user.is_authenticated else "Guest",
                phone="0000000000"
            )
            request.session['order_id'] = order.id
        else:
            order = Order.objects.get(id=order_id)

        item = MenuItem.objects.get(id=item_id)

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            item=item
        )

        if not created:
            order_item.quantity += 1
            order_item.save()

    return redirect('/menu/')


@login_required(login_url='/login/')
def cart(request):
    order_id = request.session.get('order_id')
    items = []
    total = 0

    if order_id:
        try:
            order = Order.objects.get(id=order_id, is_completed=False)
            items = OrderItem.objects.filter(order=order)

            for item in items:
                total += item.item.price

        except Order.DoesNotExist:
            request.session.pop('order_id', None)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

@login_required(login_url='/login/')
def remove_item(request, item_id):
    item = OrderItem.objects.get(id=item_id)
    item.delete()
    return redirect('/cart/')

@login_required(login_url='/login/')
def checkout(request):
    order = Order.objects.filter(
        user=request.user,
        is_completed=False
    ).first()

    if not order:
        return redirect('/menu/')

    items = OrderItem.objects.filter(order=order)

    if request.method == "POST":
        order.name = request.POST['name']
        order.phone = request.POST['phone']
        order.address = request.POST.get('address', '')
        order.is_completed = True
        order.save()

        request.session.pop('order_id', None)
        return render(request, 'order_success.html')

    return render(request, 'checkout.html', {'items': items})


@login_required(login_url='/login/')
def reserve(request):
    if request.method == "POST":
        Reservation.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests']
        )
        return render(request, 'reserve.html', {'success': True})

    return render(request, 'reserve.html')


def signup(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        login(request, user)
        return redirect('/')

    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def order_history(request):
    orders = Order.objects.filter(
        user=request.user,
        is_completed=True
    ).order_by('-id')

    return render(request, 'order_history.html', {'orders': orders})


def increase_qty(request, item_id):
    item = OrderItem.objects.get(id=item_id)
    item.quantity += 1
    item.save()
    return redirect('/cart/')


def decrease_qty(request, item_id):
    item = OrderItem.objects.get(id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('/cart/')
