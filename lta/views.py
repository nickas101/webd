from django.shortcuts import render

# Create your views here.
def lta(request):

    print("LOMAS!")
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # # Доступные книги (статус = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона lomas.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'lta.html',
        context={'num_books': 5, 'num_instances': 7,
                 'num_instances_available': 6, 'num_authors': 4},
    )

def runs(request):

    return render(
        request,
        'lta_runs.html',
        context={'num_books': 5, 'num_instances': 7,
                 'num_instances_available': 6, 'num_authors': 4},
    )


def overdue(request):

    return render(
        request,
        'lta_overdue.html',
        context={'num_books': 5, 'num_instances': 7,
                 'num_instances_available': 6, 'num_authors': 4},
    )