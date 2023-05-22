from bdb import set_trace
from django.shortcuts import render

# Create your views here.
from .models import Works,Projects,WorkStatus,WorkTypes,Product,AddCart
from rest_framework.response import Response
from rest_framework.views import APIView
import math
# Create your views here.

class Productget(APIView):
    def get(self,request):
        
        data=Product.objects.filter(int_status = 1).values("pk_bint_id","vchr_name","dbl_rate")
        lst_data =[]
        for item in data:
            dct_data ={}
            dct_data['id'] = item['pk_bint_id']
            dct_data['name'] = item['vchr_name']
            dct_data['rate'] = item['dbl_rate']
            lst_data.append(dct_data)

        print(lst_data)
        return Response(lst_data)

class TotalAmt(APIView):
    def post(self,request):
        data=AddCart.objects.filter(int_qty__gt =0).values("pk_bint_id","fk_product_id","fk_product_id__vchr_name","fk_product_id__dbl_rate","int_qty")
        lst_data10=[]
        lst_data50 =[]
        total_product=0
        total_qty=0
        if request.data:
            gift=1
        else:
            gift =0
        bln_50 = False
        for item in data:
            dct_data={}
            amount =0
            if 15>=item['int_qty']>10:
                dct_data['qty']=item['int_qty']
                dct_data['rate'] = item['fk_product_id__dbl_rate']
                lst_data10.append(dct_data)
            
            if item['int_qty']>15:
                dct_data['qty']=item['int_qty']
                dct_data['rate'] =item['fk_product_id__dbl_rate']
                lst_data50.append(dct_data)

            total_qty +=item['int_qty']
            
            total_product += item['int_qty']*item['fk_product_id__dbl_rate']
            
        bln_20=False
        bln200=False
        bln15 =False
        if total_product >200:
            total_amount200 = total_product-10
            bln200=True

        if total_qty>20:
            total_amount20 =total_product*.9
            if total_amount200>total_amount20:
                bln_20= True
                bln200=False
            else:
                bln200=True

        if lst_data10:
            total_amount15 =total_product
            for qty in lst_data10:
                
                amount = qty['qty']*qty['rate']
                total_amount15 = total_amount15-amount+(qty['qty']*(qty['rate']))*.95
            if bln200 :
                if total_amount15<total_amount200:
                    bln15=True
                    bln200=False
            elif bln_20:
                if total_amount15<total_amount20:
                    bln15=True
                    bln_20=False
        if total_qty>30:

            if lst_data50:
                total_amount50= total_product
                for qty in lst_data50:
                    
                    amount = qty['qty']*qty['rate']
                    total_amount50 =total_amount50-amount
                    total_amount50 =total_amount50+(15*qty['rate'])+((qty['qty']-15)*((qty['rate'])*.5))
                if bln15:
                    if total_amount50<total_amount15:
                        bln_50=True
                        bln15=False
                elif bln200:
                    if total_amount50<total_amount200:
                        bln_50=True
                        bln200=False
                elif bln_20:
                    if total_amount50<total_amount20:
                        bln_50 = True
                        bln_20=False


        lst_data =[]
        dct_datas ={}
        if gift ==1:
            gift_ammount =total_qty
            dct_datas['gift'] = gift_ammount
        else:
            gift_ammount=0
        num=math.ceil((total_qty)/10)
        shipping_charge=num*5
        dct_datas['shipping_charge']=shipping_charge
        if bln200:
            dct_datas['total']=total_amount200+gift_ammount+shipping_charge
            dct_datas['discount'] = total_product - total_amount200
            dct_datas['total_amount'] = total_product
            dct_datas['total_discount'] = total_amount200
            dct_datas['subtotal']=total_amount200+gift_ammount
            
            lst_data.append(dct_datas)
            return Response(lst_data)
        elif bln_20:
            dct_datas['total']=total_amount20+gift_ammount+shipping_charge
            dct_datas['discount'] = total_product-total_amount20
            dct_datas['total_amount'] = total_product
            dct_datas['total_discount'] =total_amount20
            dct_datas['subtotal']=total_amount20+gift_ammount

            lst_data.append(dct_datas)
            return Response(lst_data)
        elif bln15:
            dct_datas['total']=total_amount15+gift_ammount+shipping_charge
            dct_datas['discount']=total_product-total_amount15
            dct_datas['total_amount'] = total_product
            dct_datas['total_discount'] =total_amount15
            dct_datas['subtotal']=total_amount15+gift_ammount

            lst_data.append(dct_datas)
            return Response(lst_data)

        elif bln_50:
            dct_datas['total'] = total_amount50+gift_ammount+shipping_charge
            dct_datas['discount']= total_product-total_amount50
            dct_datas['total_amount'] = total_product
            dct_datas['total_discount'] =total_amount50
            dct_datas['subtotal']=total_amount50+gift_ammount

            lst_data.append(dct_datas)
            return Response(lst_data)
        else:
            dct_datas['total'] = total_product+gift_ammount+shipping_charge
            dct_datas['discount']= total_product-total_product
            dct_datas['total_amount'] = total_product
            dct_datas['total_discount'] =total_product
            dct_datas['subtotal']=total_product+gift_ammount

            lst_data.append(dct_datas)
            return Response(lst_data)
           

class Remove(APIView):
    def post(self,request):
        data=AddCart.objects.filter(pk_bint_id = request.data).update(int_qty=0)
        return Response(content_type=CartAdd)
class Update(APIView):
    def post(self,request):
        qty=request.data.get('int_qty')
        id=request.data.get('pk_bint_id')
        data=AddCart.objects.filter(pk_bint_id =id).update(int_qty =qty) 
        return Response(content_type=Update) 

class ApiStatus(APIView):
    def get(self,request):
        data=AddCart.objects.filter(int_qty__gt =0).values("pk_bint_id","fk_product_id","fk_product_id__vchr_name","fk_product_id__dbl_rate","int_qty")
        return Response(data)
    
class CartAdd(APIView):
    def post(self,request):
        ins_data = AddCart.objects.filter(fk_product_id = request.data,int_qty__gt =0).values('pk_bint_id','int_qty')
        
        if ins_data:
            int_qty = ins_data[0]['int_qty'] +1
            AddCart.objects.filter(pk_bint_id = ins_data[0]['pk_bint_id']).update(int_qty =int_qty)
            return Response(content_type=CartAdd)
        else:

            data = AddCart.objects.create(fk_product_id = request.data,int_qty = 1)
            data.save()
            return Response(content_type=CartAdd)
