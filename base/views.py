from django.shortcuts import render


# Home Page Views
def homePage(request):
    return render(request, 'base/homePage.html')

def registerPage(request):
    return render(request, 'base/userReg/registerPage.html' )

# Register Buddy Views

def registerDolphin(request):
    return render(request, 'base/userReg/registerDolphin.html' )

def registerTurtle(request):
    return render(request, 'base/userReg/registerTurtle.html' )

def registerWhale(request):
    return render(request, 'base/userReg/registerWhale.html' )

def registerSeal(request):
    return render(request, 'base/userReg/registerSeal.html' )

def registerSeagull(request):
    return render(request, 'base/userReg/registerSeagull.html' )


# End of Register Buddy Views


