import requests
from django.http import HttpResponse
from django.shortcuts import render
import requests as req
import json
# Create your views here.

def showindex(request):
    response = req.get('https://api.rootnet.in/covid19-in/stats/latest') #connecting to url
    #the link providing is json response
    data=response.text # but json response is in string format
    dict_data=json.loads(data)# converting json to dict data
    print((dict_data))

    if dict_data["success"]:
        return render(request, "index.html", {"information": dict_data})
    else:
        return render(request,"index.html",{"error":"Sorry..your request cannot proceed Now."})

    return HttpResponse(data)




# def showindex(request):
#
#     send_request('https://api.rootnet.in/covid19-in/stats/latest')
#     return HttpResponse("Ok")
#
#
# def send_request(url):
#    response= requests.get(url)
#   # print(response.status_code)
#    text=response.text
#   # print(text)
#    return text
def hospdetails(request):
    response = req.get('https://api.rootnet.in/covid19-in/hospitals/beds')  # connecting to url
    # the link providing is json response
    data = response.text  # but json response is in string format
    dict_data = json.loads(data)  # converting json to dict data
    print((dict_data))

    if dict_data["success"]:
        return render(request, "hospdetails.html", {"information": dict_data})
    else:
        return render(request, "hospdetails.html", {"error": "Sorry..your request cannot proceed Now."})

    return HttpResponse(data)


def detailsinfo(request):
    return render(request,'home.html')


def medical_college(request):
    response = req.get('https://api.rootnet.in/covid19-in/hospitals/medical-colleges')  # connecting to url
    # the link providing is json response
    data = response.text  # but json response is in string format
    dict_data = json.loads(data)  # converting json to dict data
    print((dict_data))

    if dict_data["success"]:
        return render(request, "medical_college.html", {"information": dict_data})
    else:
        return render(request, "medical_college.html", {"error": "Sorry..your request cannot proceed Now."})

    return HttpResponse(data)