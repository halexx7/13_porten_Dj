import datetime

from django.shortcuts import render


def main(request):
    title = "главная"
    products = [
        {
            "name": "Louis XVI ATHOS",
            "desc": "Часы премиального качества.",
            "image_src": "man_1.png",
            "image_href": "/product/1/",
            "price": 165000,
            "prop": "автоподзавод",
        },
        {
            "name": "Louis XVI ATHOS",
            "desc": "Часы премиального качества.",
            "image_src": "man_1.png",
            "image_href": "/product/2/",
            "price": 165000,
            "prop": "автоподзавод",
        },
        {
            "name": "Louis XVI ATHOS",
            "desc": "Часы премиального качества.",
            "image_src": "man_1.png",
            "image_href": "/product/3/",
            "price": 165000,
            "prop": "автоподзавод", 
        },
    ]
    content = {"title": title, "products_new": products[:3]}
    return render(request, "mainapp/index.html", content)


def product(request):
    title = "продукты"
    links_menu = [
            {"href": "product_man", "name": "мужские"},
            {"href": "product_woman", "name": "женские"},
            {"href": "product_kids", "name": "детские"},
        ]

    content = {"title": title, "links_menu": links_menu}
    return render(request, "mainapp/product.html", content)


def contacts(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@eliteclock.ru", "address": "ул.Тверская, д.1"},
        {"city": "Екатеринбург", "phone": "+7-888-888-8888", "email": "info@eliteclock.ru", "address": "ул.Карла Маркса, д.50"},
        {"city": "Ижевск", "phone": "+7-912-888-8888", "email": "info@eliteclock.ru", "address": "ул.Советская, д.90"},
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)