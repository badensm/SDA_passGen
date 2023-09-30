from django.shortcuts import render
import string, random

def password_generator(length: int,if_upper: bool, if_numbers: bool, if_special: bool):
    
    character_list = string.ascii_lowercase

    if if_upper:
        character_list = character_list + string.ascii_uppercase

    if if_numbers:
        character_list = character_list + string.digits

    if if_special:
        character_list = character_list + string.punctuation
    

    password = ''

    for _ in range(length):
        password += random.choice(character_list)
        
    return password

def home(request):
    return render(request, 'home.html')

def password(request):
    length = int(request.POST.get('length'))
    upper = request.POST.get('upper')
    numbers = request.POST.get('numbers')
    special = request.POST.get('special')

    gen_pasaword = password_generator(length, upper, numbers, special)
    return render(request, 'password.html', {'password': gen_pasaword})
