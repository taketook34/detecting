from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from PIL import Image
import easyocr

lang = ['en', 'ru', 'uk', 'de', 'es', 'fr']

class WorkForm(forms.Form):
    lang = forms.CharField(max_length=255)
    image = forms.ImageField()

def get_language(arg):
    result = arg.split(' ')
    for i in result:
        if i not in lang:
            result.remove(i)

    return result

def home(request):
    if request.method == "POST":
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            need_languages = get_language(form.cleaned_data['lang'])
            #print(need_languages)
            image_field = form.cleaned_data['image']
            image_name = './upload/image.' + image_field.image.format.lower()
            file = Image.open(image_field)
            file.save(image_name)
            reader = easyocr.Reader(need_languages)
            result = reader.readtext(image_name, detail=0, paragraph=True)
            #print(result)
            context = {
                "form": form,
                "result": result,
                "title": "Вивід з картинки на текст",
                "main": "Вивід з картинки на текст",
            }
            #return render(request, 'detecter/index.html', context=context)
    else:
        form = WorkForm()
        context = {
            "form":form,
            "title":"Вивід з картинки на текст",
            "main":"Вивід з картинки на текст",
        }
    return render(request, 'detecter/index.html', context=context)