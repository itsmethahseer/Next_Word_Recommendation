from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
import numpy as np
import tensorflow
import keras_ocr
from keras.preprocessing.text import Tokenizer
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
import os
import joblib
import pickle


model = joblib.load("myapp/models/joblib_saved_model")
tokenizer = pickle.load(open("myapp/models/my_tokenizer","rb"))


def sign(request):
    if request.user.is_authenticated:
        return render(request, 'signup.html')
    if request.method=='POST':
        uname =request.POST.get('username')
        print(uname)
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same")
        else:
            my_user =User.objects.create_user(uname,email,pass1)
            my_user.save()
            print("jhell")
        # return HttpResponse("User has been created successfully")
            return render(request, 'login.html')
        #print(uname,email,pass1,pass2)

    return render(request, 'signup.html')

@never_cache
def login_page(request):
    print("iam")
    if request.user.is_authenticated:
        return redirect('words')
    if request.method=='POST':
        print("this is login")
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        print(password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # request.session['username'] = username
            print("hai")
            login(request,user)
            return redirect('words')
        else:
            return HttpResponse("username or password is incorrect")
    return render(request, 'login.html')
@never_cache
def Logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')
def predict_next_words(request):
    text = request.GET.get('text', '    ')
    words = text.split()
    print(words)
    
    if len(words) < 3:
        return JsonResponse({'predicted_word': 'Please provide a line with at least three words.'})
    
    sequence = tokenizer.texts_to_sequences([words[-3:]])
    sequence = np.array(sequence)
    pred = np.argmax(model.predict(sequence))
    predicted_word = ""
    
    for key, value in tokenizer.word_index.items():
        if value == pred:
            predicted_word = key
            break
    
    return JsonResponse({'predicted_word': predicted_word})

def words(request):
    return render(request, 'index.html')