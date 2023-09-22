from operator import itemgetter

import requests

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url) # r -> lista zawierająca identyfikatory 500 najpopularniejszych atrykułów w wietrynie Hacker News.
print(f"Kod stanu: {r.status_code}")
print(r)

# Przetworzenie informacji o każdym artykule.
submission_ids = r.json() # Zamiana tekstu odpowiedzi na listę zawierającą id atrykułów.
submission_dicts = []
for submission_id in submission_ids[:30]: # Interesuje nas 30 pierwszych artykułów.
    # Przygotowanie oddzielnego wywołania API dla każdego artykułu.
    url = (f'https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    r = requests.get(url)
    print(r.status_code)
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])