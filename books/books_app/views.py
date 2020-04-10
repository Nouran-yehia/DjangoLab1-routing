from django.shortcuts import render
books= [{"name":"Php", "Author":"Ahmed", "details":"about php languages", "image":"php.jpeg", "id": "1" },
        {"name":"Python", "Author":"Mohamed", "details":"about Python languages", "image":"py.jpg", "id":"2" },
         {"name":"Networking", "Author":"Ibhrahim", "details":"about how to build a network with people", "image":"com.jpg", "id":"3" },
        {"name":"ITI", "Author":"Noura", "details":"life_in_iti", "image":"iti.jpeg", "id":"4" }]
    
def show_all(req):
    for book in books:
        context = {"books": books}
    return render(req, 'books_app/all.html', context)

def one_book (req, id):
    for book in books:
        if book["id"] == id:
            context={"book":book}
    return render (req, "books_app/one_book.html", context)