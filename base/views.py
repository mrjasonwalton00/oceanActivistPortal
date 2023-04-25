from django.shortcuts import render


#userReg Views
def homePage(request):
    return render(request, 'base/homePage.html')

def registerPage(request):
    return render(request, 'base/registerPage.html' )


