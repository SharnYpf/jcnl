# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import *
import os
import uuid


def index(request):
    communitys = Community.objects.order_by("name")
    return render_to_response('index.html', locals())


def community(request):
    id = request.REQUEST.get("id")
    community = Community.objects.get(id=id)
    return render_to_response('community.html', locals())


def building(request):
    id = request.REQUEST.get("id")
    is_sell = request.REQUEST.get("is_sell", None)
    building = Building.objects.get(id=id)
    if is_sell != None:
        houses = House.objects.filter(building=building, is_sell=is_sell)
    return render_to_response('building.html', locals())


def house(request):
    id = request.REQUEST.get("id")
    house = House.objects.get(id=id)
    return render_to_response('house.html', locals())


def zxcj(request):
    rs = Info.objects.filter(category="zxcj")
    return render_to_response('zxcj.html', locals())

def xqxxs(request):
    rs = Info.objects.filter(category="xqxxs")
    return render_to_response('xqxxs.html', locals())

def bmfw(request):
    rs = Info.objects.filter(category="bmfw")
    return render_to_response('bmfw.html', locals())

def wtczcs(request):
    rs = Info.objects.filter(category="wtczcs")
    return render_to_response('wtczcs.html', locals())




def admin_community(request):
    rs = Community.objects.order_by("name")
    return render_to_response('admin_community.html', locals())

def admin_community_add(request):
    name = request.REQUEST.get("name")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")
    link = request.REQUEST.get("link")

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
    else:
        url = ""

    Community(name=name, left=left, top=top, link=link, pic_url=url).save()
    return HttpResponseRedirect("/admin_community/")

def admin_community_del(request):
    id = request.REQUEST.get("id")
    Community.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_community/")

def admin_community_update(request):
    id = request.REQUEST.get("id")
    name = request.REQUEST.get("name")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")
    link = request.REQUEST.get("link")
    community = Community.objects.get(id=id)
    community.name = name
    community.left = left
    community.top = top
    community.link = link

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
        community.pic_url = url

    community.save()
    return HttpResponseRedirect("/admin_community/")



def admin_building(request):
    cid = request.REQUEST.get("cid")
    community = Community.objects.get(id=cid)
    rs = Building.objects.filter(community=community).order_by("name")
    return render_to_response('admin_building.html', locals())

def admin_building_add(request):
    cid = request.REQUEST.get("cid")
    name = request.REQUEST.get("name")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
    else:
        url = ""

    community = Community.objects.get(id=cid)
    Building(community=community, name=name, left=left, top=top, pic_url=url).save()
    return HttpResponseRedirect("/admin_building/?cid=%s"%cid)

def admin_building_del(request):
    id = request.REQUEST.get("id")
    building = Building.objects.get(id=id)
    cid = building.community.id
    building.delete()
    return HttpResponseRedirect("/admin_building/?cid=%s"%cid)

def admin_building_update(request):
    id = request.REQUEST.get("id")
    name = request.REQUEST.get("name")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")

    building = Building.objects.get(id=id)
    building.name = name
    building.left = left
    building.top = top

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
        building.pic_url = url

    building.save()
    cid = building.community.id
    return HttpResponseRedirect("/admin_building/?cid=%s"%cid)





def admin_house(request):
    bid = request.REQUEST.get("bid")
    building = Building.objects.get(id=bid)
    rs = House.objects.filter(building=building).order_by("-name")
    return render_to_response('admin_house.html', locals())

def admin_house_add(request):
    bid = request.REQUEST.get("bid")
    name = request.REQUEST.get("name")
    price = request.REQUEST.get("price")
    description = request.REQUEST.get("description")
    is_sell = request.REQUEST.get("is_sell")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")

    building = Building.objects.get(id=bid)
    house = House(building=building, name=name, price=price, description=description, is_sell=is_sell, left=left, top=top)
    house.save()

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
        Pic(house=house, url=url).save()

    return HttpResponseRedirect("/admin_house/?bid=%s"%bid)

def admin_house_del(request):
    id = request.REQUEST.get("id")
    house = House.objects.get(id=id)
    bid = house.building.id
    house.delete()
    return HttpResponseRedirect("/admin_house/?bid=%s"%bid)

def admin_house_update(request):
    id = request.REQUEST.get("id")
    name = request.REQUEST.get("name")
    price = request.REQUEST.get("price")
    description = request.REQUEST.get("description")
    is_sell = request.REQUEST.get("is_sell")
    left = request.REQUEST.get("left")
    top = request.REQUEST.get("top")

    house = House.objects.get(id=id)
    house.name = name
    house.price = price
    house.description = description
    house.is_sell = is_sell
    house.left = left
    house.top = top
    house.save()

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
        Pic(house=house, url=url).save()

    bid = house.building.id
    return HttpResponseRedirect("/admin_house/?bid=%s"%bid)



def admin_pic_del(request):
    id = request.REQUEST.get("id")
    pic = Pic.objects.get(id=id)
    bid = pic.house.building.id
    pic.delete()
    return HttpResponseRedirect("/admin_house/?bid=%s"%bid)





def admin_info(request):
    category = request.REQUEST.get("category")
    rs = Info.objects.filter(category=category)
    return render_to_response('admin_info.html', locals())

def admin_info_add(request):
    category = request.REQUEST.get("category")
    title = request.REQUEST.get("title")
    content = request.REQUEST.get("content")
    link = request.REQUEST.get("link")

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
    else:
        url = ""

    Info(category=category, title=title, content=content, link=link, pic_url=url).save()
    return HttpResponseRedirect("/admin_info/?category=" + category)

def admin_info_del(request):
    id = request.REQUEST.get("id")
    info = Info.objects.get(id=id)
    category = info.category
    category.delete()
    return HttpResponseRedirect("/admin_info/?category=" + category)

def admin_info_update(request):
    id = request.REQUEST.get("id")
    title = request.REQUEST.get("title")
    content = request.REQUEST.get("content")
    link = request.REQUEST.get("link")
    info = Info.objects.get(id=id)
    info.title = title
    info.content = content
    info.link = link

    pic = request.FILES.get("pic")
    if pic:
        filename =  pic.name
        ext = filename.split(".")[-1]
        if ext.lower() not in ["jpg", "bmp", "png", "gif", "jpeg"]:
            return HttpResponse("请上传正确的图片文件")
        filename = "%s.%s" % (uuid.uuid4(), ext.lower())
        if 'SERVER_SOFTWARE' in os.environ:
            import sae.storage
            s = sae.storage.Client()
            p = sae.storage.Object(pic.read())
            url = s.put('pic', filename, p)
        else:
            raw_file = os.path.join(os.getcwd(), 'static', 'images', 'pic', filename)
            f = open(raw_file, 'wb+')
            for chunk in pic.chunks():
                f.write(chunk)
            f.close()
            url = "/static/images/pic/" + filename
        info.pic_url = url

    info.save()
    category = info.category
    return HttpResponseRedirect("/admin_info/?category=" + category)



def admin_user(request):
    rs = User.objects.all()
    return render_to_response('admin_user.html', locals())

def admin_user_active(request):
    id = request.REQUEST.get("id")
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect("/admin_user/")

def admin_user_super(request):
    id = request.REQUEST.get("id")
    user = User.objects.get(id=id)
    user.is_superuser = True
    user.save()
    return HttpResponseRedirect("/admin_user/")

def admin_user_del(request):
    id = request.REQUEST.get("id")
    User.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin_user/")



#==================== auth ===========================================

def loginpage(request):
    return render_to_response('loginpage.html', locals())

def registerpage(request):
    return render_to_response('registerpage.html', locals())

def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/")

def register(request):
    msg = ""
    username = request.REQUEST.get('username')
    password1 = request.REQUEST.get('password1')
    password2 = request.REQUEST.get('password2')
    if username and password1 and password2:
        if User.objects.filter(username=username):
            msg = "该用户名已被注册"
            return render_to_response('registerpage.html', locals())
        if password1 == password2:
            user = User()
            user.username = username
            user.set_password(password1)
            user.is_active = False
            user.save()
            msg = "注册成功,请等待通过管理员审批"
            return render_to_response('registerpage.html', locals())
    msg = "输入有误，请重新输入"
    return render_to_response('registerpage.html', locals())

#======================================================================




# ===================== helper ==========================
def initdb(request):
    from django.core.management import execute_from_command_line
    execute_from_command_line(["initdb", "syncdb"])
    return HttpResponse("initdb ok")



