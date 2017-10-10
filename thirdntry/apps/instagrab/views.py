from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from thirdntry.apps.instagrab.models import Instagraminfo
# Create your views here.

def index(request):
    insta_db = Instagraminfo.objects.all()
    context= {
        'insta':insta_db
    }
    return render(request, "index.html", context)



def token():
    # get page
    response = urllib.request.urlopen(
        'https://api.instagram.com/v1/users/self/media/recent/?access_token=2206414601.3460b84.9cb29545fe194f1ea13b28d8b60cc479')
    # read JSON file
    data = json.load(response)
    # get number of images by len of 'data'
    list_long = len(data['data'])
    for img_num in range(0, list_long):
        # get img
        image_url = data['data'][img_num]['images']['standard_resolution']['url']
        # get tags
        tag_name = data['data'][img_num]['tags']
        # prim_key must start from 1, so
        img_num += 1
        # add image and tags to console with id
        add_image_db = Instagraminfo(id=img_num, image_ins=image_url, tag_ins=tag_name)
        # add fron console to db
        add_image_db.save()
