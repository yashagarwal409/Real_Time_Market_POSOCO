from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import bidform, rtmform
from buyer.models import Reserve
import datetime
#from datetime import datetime, time
from django.utils import timezone
from django.conf import settings
from buyer.models import TimeBlock, ClearEntityDown, ClearEntityUp
User = settings.AUTH_USER_MODEL


def is_time_between(begin_time, end_time):
    # If check time is not given, default to current UTC time
    check_time = timezone.localtime(timezone.now()).time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:  # crosses midnight
        return check_time >= begin_time or check_time <= end_time
# Create your views here.


def home(response):
    return render(response, 'seller/home.html', {})


def rtm(response):
    return render(response, 'seller/rtm.html', {})


def dat(response):
    return render(response, 'seller/dat.html', {})


def displaydata(response):
    return render(response, 'seller/displaydata.html', {})


def placebid(response, rtmordat, upordown):
    is_rtm = False
    is_up = False
    is_dat = False
    is_down = False
    if rtmordat == "rtm":
        is_rtm = True
    if rtmordat == "dat":
        is_dat = True
    if upordown == "up":
        is_up = True
    if upordown == "down":
        is_down = True
    if response.method == "POST":
        form = bidform(response.POST)
        user = response.user
        if form.is_valid():
            user.bid_set.create(
                time=form.cleaned_data['time'], volume=form.cleaned_data['volume'], price=form.cleaned_data['price'], is_up=is_up, is_down=is_down, is_rtm=is_rtm, is_dat=is_dat, date=form.cleaned_data['date'])
    else:
        form = bidform()
    return render(response, 'seller/placebid.html', {"form": form})


def rtmbid(response, upordown):
    is_rtm = False
    is_up = False
    is_dat = False
    is_down = False
    form = None
    if upordown == "up":
        is_up = True
    if upordown == "down":
        is_down = True
    if response.method == "POST":
        user = response.user
        user.bid_set.create(
            time=response.POST.get('time'), date=response.POST.get('date'), volume=response.POST.get('volume'), price=response.POST.get('price'), is_up=is_up, is_down=is_down, is_rtm=True, is_dat=False)
        return render(response, 'buyer/message.html', {"message": "The Bid has been placed successfully!"})
    objectlist = TimeBlock.objects.all()
    timelist = []
    for object in objectlist:
        timelist.append(object.time)
    for i in range(1, 96, 2):
        times = timelist[i]
        begt = datetime.datetime.strptime(times[0:5], '%H:%M').time()
        if i != 95:
            endt = datetime.datetime.strptime(times[6:11], '%H:%M').time()
        else:
            endt = datetime.datetime.strptime('00:00', '%H:%M').time()
        if(is_time_between(begt, endt)):
            form = rtmform(
                timeoptions=[timelist[(i+5) % 96], timelist[(i+6) % 96]])
            break
    if form == None:
        return render(response, 'seller/message.html', {"message": "Please login after a while. The portal is down."})
    return render(response, 'seller/placebid.html', {'form': form})


def datbid(response, upordown):
    is_rtm = False
    is_up = False
    is_dat = False
    is_down = False
    form = None
    if upordown == "up":
        is_up = True
    if upordown == "down":
        is_down = True
    objectlist = Reserve.objects.filter(name='AGBPP-GAS').order_by('time')
    timelist = []
    for object in objectlist:
        timelist.append(object.time)
    form = rtmform(
        timeoptions=timelist)
    if response.method == "POST":
        user = response.user
        user.bid_set.create(
            time=response.POST.get('time'), date=response.POST.get('date'), volume=response.POST.get('volume'), price=response.POST.get('price'), is_up=is_up, is_down=is_down, is_rtm=False, is_dat=True)
        return HttpResponse("Data Entered into the Database successfully!")

    return render(response, 'seller/placebid.html', {'form': form})


def datbidlist(response, upordown):
    if response.method == 'POST':
        is_rtm = False
        is_up = False
        is_dat = False
        is_down = False
        user = response.user
        form = response.POST
        if upordown == "up":
            is_up = True
        if upordown == "down":
            is_down = True
        for time in TimeBlock.objects.all():
            qid = 'q'+str(time.id)
            pid = 'p'+str(time.id)
            quantity = response.POST.get(qid)
            price = response.POST.get(pid)
            if float(quantity) > 0 and float(price) > 0:
                user.bid_set.create(time=time.time, date=response.POST.get(
                    'date'), volume=quantity, price=price, is_up=is_up, is_down=is_down, is_rtm=False, is_dat=True)

        return render(response, 'buyer/message.html', {"message": "The data has been entered successfully!."})
    else:
        return render(response, "seller/datform.html", {'timeblock': TimeBlock.objects.all()})


def cleardataup(response, rtmordat):
    user = response.user
    is_rtm = False
    is_up = False
    is_dat = False
    is_down = False
    if rtmordat == "rtm":
        is_rtm = True
    if rtmordat == "dat":
        is_dat = True
    objects = ClearEntityUp.objects.all().filter(name=user.username,
                                                 clearedreserve__is_rtm=is_rtm, clearedreserve__is_dat=is_dat).order_by('clearedreserve__time_block').order_by('clearedreserve__date')
    return render(response, 'seller/clearedupdata.html', {"objects": objects})


def cleardatadown(response, rtmordat):
    user = response.user
    is_rtm = False
    is_up = False
    is_dat = False
    is_down = False
    if rtmordat == "rtm":
        is_rtm = True
    if rtmordat == "dat":
        is_dat = True
    objects = ClearEntityDown.objects.all().filter(name=user.username,
                                                   clearedreserve__is_rtm=is_rtm, clearedreserve__is_dat=is_dat).order_by('clearedreserve__date').order_by('clearedreserve__time_block')
    return render(response, 'seller/cleareddowndata.html', {"objects": objects})
