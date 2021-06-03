from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    diction = {}
    if request.method == 'POST':
        search = request.POST.get('search')
        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        print(meaning)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)
        diction.update({'meaning':meaning['Noun'][0], 'synonyms':synonyms, 'antonyms':antonyms})
    return render(request, 'index.html', context=diction)
