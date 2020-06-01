# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import EruzMember
from .models import NalogCodes
from .models import Okved2020
from .models import BossPerson
# from .models import AuthUser
# from .serializers import AuthUserSerializer
# from rest_framework import viewsets
# from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator
import re

from bitrix24 import *





# bx24 = Bitrix24('https://expertcentre.bitrix24.ru/rest/98/xltjo04ombaofhez')

bx24 = Bitrix24('https://expertcentre.bitrix24.ru/rest/104/9ggcm229ba4niyv2')



region = ""
gorod = ""
okved = ""
companyname = ""
bossname = ""
inn = ""
inn2 = ""
inntotal = ""
phone = ""
cell = ""
email = ""
phonetotal = ""
recordsperpage = 10
nalogCodes = ""
nalogCodes2 = ""
okved2020 = ""
eruzMember = ""
bossPerson = ""
current_user_email = ""
current_user_bitrix_id = ""
generalRequest = ""

# class AuthUserView(viewsets.ModelViewSet):
#     queryset = AuthUser.objects.all()
#     serializer_class = AuthUserSerializer

@login_required(login_url="/login/")
def index(request):
    from django.db.models import Q


    global region
    global gorod
    global okved
    global companyname
    global bossname
    global inn
    global inn2
    global inntotal
    global phone
    global cell
    global email
    global recordsperpage
    global phonetotal
    global nalogCodes
    global nalogCodes2
    global okved2020
    global eruzMember
    global eruzMembers
    global bossPerson
    global bx24
    global current_user_email
    global generalRequest
    global current_user_bitrix_id
    leadId = ""
    newBitrixLeadObject = ""
    current_user_email = request.user.email

    if eruzMember == "" or eruzMember is None:
        eruzMember = EruzMember.objects.latest('id')
    # eruzMembers = EruzMember.objects.all().order_by('-id')[:20]
    if bossPerson == "" or bossPerson is None:
        bossPerson = BossPerson.objects.latest('id')

    if not current_user_bitrix_id:
        try:
            api_request_current_user = bx24.callMethod('user.get',
                                               filter={'EMAIL': request.user.email},
                                               select=['ID'])
        except BitrixError as message:
            print(message)
        except:
            pass

        if api_request_current_user:
            api_request_current_user = api_request_current_user[0]
                # print(api_request_current_user)
            current_user_bitrix_id = api_request_current_user["ID"]




    if nalogCodes == "" or nalogCodes is None:
        nalogCodes = NalogCodes.objects.all().filter(nalog_kod__endswith='00').order_by('id')
    if nalogCodes2 == "" or nalogCodes2 is None:
        nalogCodes2 = NalogCodes.objects.order_by('nalog_city').values('nalog_city').distinct()

    if okved2020 == "" or okved2020 is None:
        okved2020 = Okved2020.objects.all().filter(okved_code__regex=r'^.{4}$')

    # if request.method == 'GET':
    #     try:
    #         generalRequest = request.GET['generalRequest']
    #         print(generalRequest)
    #     except:
    #         pass

    if request.method == 'POST':
        try:
            generalRequest = request.POST['generalRequest']
            # print(generalRequest)
            if generalRequest:
                region = ""
                gorod = ""
                okved = ""
                bossname = ""
                companyname = ""
                inn = ""
                inn2 = ""
                phone = ""
                cell = ""
                email = ""

                eruzMembers = EruzMember.objects.filter(Q(nalog_codes_id__nalog_region__icontains=generalRequest) |
                                                        Q(nalog_codes_id__nalog_city__icontains=generalRequest) |
                                                        Q(main_okved__icontains=generalRequest) |
                                                        Q(company_address__icontains=generalRequest) |
                                                        Q(main_okved_desc__icontains=generalRequest) |
                                                        Q(boss_person_id__l_name__icontains=generalRequest) |
                                                        Q(full_company_name__icontains=generalRequest) |
                                                        Q(eruz_member_inn__contains=generalRequest) |
                                                        Q(boss_person_id__boss_inn__contains=generalRequest) |
                                                        Q(company_phone__contains=generalRequest) |
                                                        Q(company_cell__contains=generalRequest) |
                                                        Q(company_email__contains=generalRequest)).order_by('-id')



                paginator = Paginator(eruzMembers, recordsperpage)
                page = request.GET.get('page')
                eruzMembers = paginator.get_page(page)
                BitrixAPI(eruzMembers, current_user_email)

                return render(request, "index.html",
                              {'eruzMember': eruzMember, 'eruzMembers': eruzMembers, 'nalogCodes': nalogCodes,
                               'nalogCodes2': nalogCodes2, 'okved2020': okved2020,
                               'region': region, 'gorod': gorod, 'okved': okved, 'companyname': companyname,
                               'bossname': bossname, 'inn': inntotal,
                               'phone': phonetotal, 'email': email, 'bossPerson': bossPerson,
                               'newBitrixLeadObject': newBitrixLeadObject, })
        except:
            pass

        try:
            leadId = request.POST['leadId']
            # print(leadId)
            # AddBitrixLeadToCurrentUser(leadId, current_user_bitrix_id)
        except:
            pass
        if leadId:
            AddBitrixLeadToCurrentUser(leadId, current_user_bitrix_id)
            # newBitrixLeadObject = AddBitrixLeadToCurrentUser(leadId, current_user_bitrix_id)
        else:
            # newBitrixLeadObject = ""
            pass


        try:
            recordsperpage2 = request.POST['recordsperpage']
            recordsperpage = int(recordsperpage2)
        except:
            pass
        region2 = ""
        try:
            region2 = request.POST['region']
            region = region2
            if region == "РФ":
                region = " "
        except:
            pass

        if not region or region is None:
            region = " "
        try:
            gorod2 = request.POST['gorod']
            gorod = gorod2
            if gorod == "Любой город":
                gorod = ""

        except:
            pass
        if not gorod or gorod is None:
            gorod = " "
        try:
            okved2 = request.POST['okved']
            okved = okved2
            if okved == "Любой вид деятельности":
                okved = ""
        except:
            pass
        if okved:
            okved = okved[0:4]
        try:
            companyname2 = request.POST['companyname']
            companyname = companyname2
        except:
            pass
        if not companyname:
            companyname = " "
        try:
            bossname2 = request.POST['bossname']
            bossname = bossname2
        except:
            pass

        try:
            inn23 = request.POST['inn']
            inntotal = inn23
            inn = inn23
        except:
            pass

        if len(inn) == 12:
            inn2 = inn
            inn = ""
            inntotal = inn
        try:
            phone2 = request.POST['phone']
            phone = phone2
            if phone:
                phone = phone.replace(" ", "")
                phone = phone.replace(")", "")
                phone = phone.replace("(", "")
                phone = phone.replace("-", "")
                phone = phone.replace("+", "")
                phone = re.sub(r'^8', '7', phone)
                phonetotal = phone
                cell = re.match("^79\d*", phone)
                if cell:
                    cell = phone
                    phone = ""
                    phonetotal = cell

                else:
                    cell = ""

        except:
            pass






        try:
            email2 = request.POST['email']
            email = email2
        except:
            pass

        eruzMembers = EruzMember.objects.all().filter(nalog_codes_id__nalog_region__contains=region,
                                                      nalog_codes_id__nalog_city__contains=gorod, main_okved__startswith=okved,
                                                      boss_person_id__l_name__icontains=bossname,
                                                      full_company_name__icontains=companyname, eruz_member_inn__contains=inn,
                                                      boss_person_id__boss_inn__contains=inn2,
                                                      company_phone__contains=phone, company_cell__contains=cell,
                                                      company_email__contains=email,).order_by('-id')






        paginator = Paginator(eruzMembers, recordsperpage)
        page = request.GET.get('page')
        eruzMembers = paginator.get_page(page)
        BitrixAPI(eruzMembers, current_user_email)

        return render(request, "index.html", {'eruzMember': eruzMember, 'eruzMembers': eruzMembers, 'nalogCodes': nalogCodes, 'nalogCodes2': nalogCodes2, 'okved2020': okved2020,
                                              'region': region, 'gorod': gorod, 'okved': okved, 'companyname': companyname, 'bossname': bossname, 'inn': inntotal,
                                              'phone': phonetotal, 'email': email, 'bossPerson': bossPerson, 'newBitrixLeadObject': newBitrixLeadObject, })



    else:

        if generalRequest:
            eruzMembers = EruzMember.objects.filter(Q(nalog_codes_id__nalog_region__icontains=generalRequest) |
                                                    Q(nalog_codes_id__nalog_city__icontains=generalRequest) |
                                                    Q(main_okved__icontains=generalRequest) |
                                                    Q(company_address__icontains=generalRequest) |
                                                    Q(main_okved_desc__icontains=generalRequest) |
                                                    Q(boss_person_id__l_name__icontains=generalRequest) |
                                                    Q(full_company_name__icontains=generalRequest) |
                                                    Q(eruz_member_inn__contains=generalRequest) |
                                                    Q(boss_person_id__boss_inn__contains=generalRequest) |
                                                    Q(company_phone__contains=generalRequest) |
                                                    Q(company_cell__contains=generalRequest) |
                                                    Q(company_email__contains=generalRequest)).order_by('-id')


        elif region or gorod or okved or bossname or companyname or inn or inn2 or phone or cell or email:
            eruzMembers = EruzMember.objects.all().filter(nalog_codes_id__nalog_region__contains=region,
                                                          nalog_codes_id__nalog_city__contains=gorod,
                                                          main_okved__startswith=okved,
                                                          boss_person_id__l_name__icontains=bossname,
                                                          full_company_name__icontains=companyname,
                                                          eruz_member_inn__contains=inn,
                                                          boss_person_id__boss_inn__contains=inn2,
                                                          company_phone__contains=phone, company_cell__contains=cell,
                                                          company_email__contains=email, ).order_by('-id')

        else:
            eruzMembers = EruzMember.objects.all().order_by('-id')

        paginator = Paginator(eruzMembers, recordsperpage)
        page = request.GET.get('page')
        eruzMembers = paginator.get_page(page)
        BitrixAPI(eruzMembers, current_user_email)



        return render(request, "index.html", {'eruzMember': eruzMember, 'eruzMembers': eruzMembers, 'nalogCodes': nalogCodes, 'nalogCodes2': nalogCodes2, 'okved2020': okved2020,
                                              'region': region, 'gorod': gorod, 'okved': okved, 'companyname': companyname, 'bossname': bossname, 'inn': inntotal,
                                              'phone': phonetotal, 'email': email, 'bossPerson': bossPerson, 'newBitrixLeadObject': newBitrixLeadObject, })



def AddBitrixLeadToCurrentUser(leadId, current_user_bitrix_id):

    leadId = int(leadId)
    newBitrixLeadObject = EruzMember.objects.get(id=leadId)
    # print(newBitrixLeadObject.id)


    if newBitrixLeadObject.id:
        if newBitrixLeadObject.short_company_name:
            title = "Ультра ЕРУЗ | " + newBitrixLeadObject.short_company_name
        elif newBitrixLeadObject.full_company_name:
            title = "Ультра ЕРУЗ | " + newBitrixLeadObject.full_company_name
        else:
            title = "УльтраЕРУЗ | ИП " + newBitrixLeadObject.boss_person_id.l_name

        source_description = "UltraERUZ"
        created_by_id = 104

        if newBitrixLeadObject.company_cell:
            phone = newBitrixLeadObject.company_cell
        elif newBitrixLeadObject.company_phone:
            phone = newBitrixLeadObject.company_phone
        else:
            phone = ""

        if newBitrixLeadObject.company_address:
            address = newBitrixLeadObject.company_address
        else:
            address = ""

        if newBitrixLeadObject.boss_person_id:
            comment = newBitrixLeadObject.boss_person_id.full_name + newBitrixLeadObject.main_okved_desc
        else:
            comment = newBitrixLeadObject.full_company_name

        if newBitrixLeadObject.short_company_name:
            companyname2 = newBitrixLeadObject.short_company_name
        elif newBitrixLeadObject.full_company_name:
            companyname2 = newBitrixLeadObject.full_company_name
        else:
            companyname2 = "ИП " + newBitrixLeadObject.boss_person_id.l_name

        if newBitrixLeadObject.eruz_member_inn:
            companyINN = newBitrixLeadObject.eruz_member_inn
        else:
            companyINN = newBitrixLeadObject.boss_person_id.boss_inn

        if newBitrixLeadObject.main_okved:
            mainokved = newBitrixLeadObject.main_okved
            mainokveddesc = newBitrixLeadObject.main_okved_desc
        else:
            mainokved = ""
            mainokveddesc = ""

        if newBitrixLeadObject.boss_person_id.f_name:
            name = newBitrixLeadObject.boss_person_id.f_name
            last_name = newBitrixLeadObject.boss_person_id.l_name
            second_name = newBitrixLeadObject.boss_person_id.s_name
        else:
            name = ""
            last_name = ""
            second_name = ""



        # print(title)

        try:
            bx24.callMethod('crm.lead.add',
                            fields={'TITLE': title, 'ASSIGNED_BY_ID': current_user_bitrix_id,
                                    'CREATED_DY_ID': created_by_id, 'SOURCE_DESCRIPTION': source_description,
                                    'EMAIL': [{'VALUE': newBitrixLeadObject.company_email, 'VALUE_TYPE': 'WORK'}],
                                    'PHONE': [{'VALUE': phone, 'VALUE_TYPE': 'WORK'}], 'ADDRESS': address, 'COMMENTS': comment,
                                    'COMPANY_TITLE': companyname2, 'UF_CRM_INN': companyINN,
                                    'UF_CRM_MAINOKVED': mainokved, 'UF_CRM_MAINOKVEDDESC': mainokveddesc, 'NAME': name, 'LAST_NAME': last_name, 'SECOND_NAME': second_name})

        except BitrixError as message:
            print(message)
        except:
            pass

        # return newBitrixLeadObject




def BitrixAPI(eruzMembers, current_user_email):
    for e in eruzMembers:
        # print(e.company_email)
        # if not e.manager_name:
        e.manager_name = ""
        e.manager_last_name = ""
        # if not e.manager_id:
        e.manager_id = ""
        e.manager_email = "verstandung1560"


        if e.company_email:
            # api_request = bx24.callMethod('crm.lead.list',
            #                               filter={'LOGIC': 'OR', 'EMAIL': e.company_email, 'PHONE': e.company_cell, 'PHONE': e.company_phone, 'UF_CRM_INN': e.boss_person_id.boss_inn, 'UF_CRM_INN': e.eruz_member_inn},
            #                             select=['ASSIGNED_BY_ID', ])
            api_request = bx24.callMethod('crm.lead.list',
                                          filter={'EMAIL': e.company_email},
                                        select=['ASSIGNED_BY_ID'])


        # if not e.manager_name:
        #     e.manager_name = ""
        #     e.manager_last_name = ""
        # if not e.manager_id:
        #     e.manager_id = ""


        if api_request:
            api_request = api_request[0]
            e.manager_id = api_request['ASSIGNED_BY_ID']

            api_request_user = ""
            if e.manager_id:
                api_request_user = bx24.callMethod('user.get',
                                              filter={'ID': e.manager_id},
                                              select=['LAST_NAME', 'NAME', 'EMAIL',])

                if api_request_user:
                    api_request_user = api_request_user[0]

                    e.manager_last_name = api_request_user['LAST_NAME']
                    e.manager_name = api_request_user['NAME']
                    e.manager_email = api_request_user['EMAIL']

                    # print(e.manager_email, current_user_email)


        else:
            e.manager_id = ""

        e.current_user_email = current_user_email


        if e.company_email and e.manager_email != current_user_email:
            try:
                e.company_email2 = "****" + e.company_email[4:]
            except:
                pass
        else:
            e.company_email2 = e.company_email

        if e.company_phone and e.manager_email != current_user_email:
            try:
                e.company_phone2 = e.company_phone[0:7] + "****"
            except:
                pass
        else:
            e.company_phone2 = e.company_phone

        if e.company_cell and e.manager_email != current_user_email:
            try:
                e.company_cell2 = e.company_cell[0:7] + "****"
            except:
                pass
        else:
            e.company_cell2 = e.company_cell






@login_required(login_url="/login/")
def pages(request):
    context = {}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

# def EruzMembers(request):
