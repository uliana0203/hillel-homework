import string
import time
import numpy as np
from django.http import HttpResponse, JsonResponse, QueryDict
from django_user_agents.utils import get_user_agent

# Create your views here.
def whoami(request):
    request.method == 'POST'
    ip_address = request.META.get('REMOTE_ADDR')
    time_on_server = time.strftime('%H:%M:%S %d %B %Y ')
    user_browser = get_user_agent(request)
    return HttpResponse(f"Current time on server: {time_on_server}, Current IP-address: {ip_address}, "
                        f"User browser: {user_browser}")
def source_code(request):
    WORDS = []
    file = open("./about/views.py")
    for line in file.readlines():
        WORDS.append(line.rstrip())
    words = [word for word in WORDS]
    return JsonResponse(words, safe=False)


def random(request):
    global gen_string
    query_dict = request.GET
    a = int(query_dict.get('length'))
    specials = int(query_dict.get(key='specials', default=0))
    digits = int(query_dict.get(key='digits',default=0))
    if a in range(1, 100):
        gen_string = string.ascii_uppercase
    if specials in range(0,2) and specials == 1:
        gen_string += '!"№;%:?*()_+'
    if digits in range(0,2) and digits == 1:
        gen_string += '0123456789'
    random_symbols = np.random.randint(1, len(gen_string), a)
    result = ''.join([gen_string[i] for i in random_symbols])
    return HttpResponse(result)
