from django.http import Http404
from django.shortcuts import get_object_or_404, render
from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()  # Это предполагает, что ваша модель называется Car

    # Передаем список автомобилей в шаблон
    context = {
        'cars': cars,
    }
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    # Используем get_object_or_404 для проверки существования автомобиля
    car = get_object_or_404(Car, pk=car_id)

    # Передаем объект автомобиля в шаблон
    context = {'car': car}
    template_name = 'main/details.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def sales_by_car(request, car_id):
    try:
        # Получаем автомобиль по идентификатору или возвращаем 404
        car = get_object_or_404(Car, pk=car_id)

        # Извлекаем все продажи данного автомобиля
        sales = Sale.objects.filter(car=car)

        # Передаем автомобиль и список продаж в шаблон
        context = {
            'car': car,
            'sales': sales
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
