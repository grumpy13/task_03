from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    restaurants = [
    {
        "restaurant_name" : "mac",
        "food_type" : "burgers"
    },
    {
        "restaurant_name" : "pastamania",
        "food_type" : "pasta"
    },
    {
        "restaurant_name" : "Kababji",
        "food_type" : "shish kabab"
    }
    ]

    context = {
                "my_list": restaurants

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    restaurant = { "restaurant_name" : "PizzaHut",
    "food_type" : "pizza",
    "prices": "300KD"
    }

    context = { "my_object": restaurant

    }
    return render(request, 'detail.html', context)
