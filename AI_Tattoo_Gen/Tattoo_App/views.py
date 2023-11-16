from django.http import HttpResponse
from django.shortcuts import render
from .open_ai_code import generate_tattoo
import requests




def home(request):
    error_message = None
    image_url_list = None
    if request.method == 'POST':
        prompt = request.POST.get('prompt', None)
        prompt += " generate a tattoo design for: " + prompt
        try:
            image_url_list = generate_tattoo(prompt)
            for image_url in image_url_list:
                print(f"[Home]\n[URL:]{image_url}\n")

        except Exception as e:
            print(f"An error occurred: {e}")
            error_message = "Sorry, something went wrong."

    context = {
        'image_url_list': image_url_list,
        'error_message': error_message,
    }
    return render(request, 'Tattoo_App/home.html', context)


def download_image(request):
    image_url = request.GET.get('image_url', None)

    if image_url:
        response = requests.get(image_url)
        content_type = response.headers['content-type']
        response = HttpResponse(response.content, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="generated_tattoo.png"'
        return response
    else:
        return render(request, 'Tattoo_App/error.html', {'error_message': 'Image URL not found'})
