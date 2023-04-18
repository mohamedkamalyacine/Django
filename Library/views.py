from django.shortcuts import render

# Create your views here.
def welcome(request, clientName):
    writersNames = ['William Shakspeare', 'J. K. Rowling', 'Agatha Cristie', 'Naguib Mahfouz']
    context = {
        "clientNameHTML" : clientName,
        "writersNamesHTML" : writersNames
    }
    return render(request, 'index.html', context)

def writerInfo(request, clientName, writerName):
    context = {
        "clientNameHTML" : clientName,
        "writerNameHTML" : writerName
    }
    return render(request, 'view_writer.html', context)