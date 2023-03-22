from django.shortcuts import render, redirect
from main.forms import *
from main.models import *
from django.db import connections
# Create your views here.


def register(request):
    if request.method == 'POST':
        c_form = CustomerForm(request.POST)
        add_form = AddressForm(request.POST)
        if c_form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            age = request.POST.get('age')
            date_of_birth = request.POST.get('date_of_birth')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

        if add_form.is_valid():
            address = add_form.save()
            cursor = connections['default'].cursor()
            try:
                cursor.execute(
                    "SELECT id FROM main_address ORDER BY id DESC LIMIT 1")
                last_insert_id = dictfetchall(cursor)
                cursor.execute("INSERT INTO main_customer(first_name,last_name,age,date_of_birth,phone,email,address_id) VALUES( %s , %s ,%s , %s , %s , %s ,%s)", [
                               first_name, last_name, age, date_of_birth, phone, email, last_insert_id[0]['id']])
            finally:
                cursor.close()
            return redirect('/cars')
    else:
        c_form = CustomerForm()
        add_form = AddressForm()
    return render(request, 'main/home.html', {'c_form': c_form, 'add_form': add_form})


def cars(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register')
    else:
        form = CarForm()
    return render(request, 'main/car.html', {'form': form})


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
