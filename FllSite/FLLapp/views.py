from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Center,Animal,Lab
# Create your views here.
def index(request):
        template=loader.get_template('FLLapp/index.html')
        return HttpResponse(template.render({},request))
def aboutcenter(request,centerid):
        center=Center.objects.get(pk=centerid)
        context={'name':
                 center.name,
                 'desc':
                 center.desc,
                 'phone':
                 center.phone,
                 'site':center.site,
                 'animals':
                 'Rodents: '+['No','Yes'][center.acceptsrodents]+'\n'+
                 'Dogs/cats: '+['No','Yes'][center.acceptsrodents]+'\n'+
                 'Primates: '+['No','Yes'][center.acceptsrodents]+'\n',
                  'state':center.state}
        template=loader.get_template('FLLapp/aboutcenter.html')
        return HttpResponse(template.render(context,request))
def search(request):
        template=loader.get_template('FLLapp/search.html')
        states=[]
        for a in Center.objects.all():
                if a.state not in states:
                        states.append(a.state)
        context={'states':sorted(states)}
        return HttpResponse(template.render(context,request))
def searchresults(request):
        template=loader.get_template('FLLapp/searchresults.html')
        params=request.GET
        req={'state':params['state']}
        if 'acc1' in params:
                req['acceptsrodents']=True
        if 'acc2' in params:
                req['acceptsdogscats']=True
        if 'acc3' in params:
                req['acceptsprimates']=True
        if 'acc4' in params:
                req['acceptsbirds']=True
        centers=Center.objects.all().filter(**req)
        newcenters=[[]]
        for a in centers:
                if len(newcenters[-1])==6:
                        newcenters.append([])
                newcenters[-1].append(['full',a.name,a.id])
        for a in range((6-len(newcenters[-1]))):
                newcenters[-1].append(['empty','',False])
        return HttpResponse(template.render({'results':newcenters,'empty':len(centers)==0},request))
def aboutlab(request,labid):
        template=loader.get_template('FLLapp/aboutcenter.html')
        context={'lab':Lab.objects.get(pk=labid)}
        return HttpResponse(template.render(context),request)
def animal(request,animalid):
        template.loader.get_template('FLLapp/animal.html')
        animal=:Animals.objects.get(pk=animalid)
        context={'animal':animal,
            gender:['Male','Female','Unknown'],
            kind:['rodent','dog','cat','primate','other'][animal.species],
            domestic:['No','Yes'][animal.domestic],
            adopted:['No','Yes'][animal.adopted],}
