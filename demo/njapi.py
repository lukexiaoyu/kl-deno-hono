from ninja import NinjaAPI
from django.http import HttpResponse
from peo.models import Peo
from car.models import Car
from ninja import ModelSchema
from typing import List

app=NinjaAPI()


class PeoSchema(ModelSchema):
    class Meta:
        model=Peo
        fields="__all__"
#单个查询
@app.get("peo/{peo_id}",response=PeoSchema)
def get_peo_id(request,peo_id:int):
    peo=Peo.objects.get(id=peo_id)
    return peo


#获取全部
@app.get("peo",response=List[PeoSchema])
def get_all(request): 
    peo=Peo.objects.all()
    return peo

#添加数据
@app.post("peo")
def c_peo(request,peo:PeoSchema):
    peo=Peo.objects.create(**peo.dict())
    return {"id":peo.id}

#更新数据
@app.put("peo/{peo_id}")
def u_peo(request,peo_id:int,u_peo:PeoSchema):
    peo=Peo.objects.get(id=peo_id)
    for attr,value in u_peo.dict().items():
        setattr(peo,attr,value)
    peo.save()
        
    return {"id":peo.id}

#删除数据
@app.delete("peo/{peo_id}")
def d_peo(request,peo_id:int): 
    peo=Peo.objects.get(id=peo_id)
    peo.delete()
    return HttpResponse("删除成功")



#car crud


class CarSchema(ModelSchema):
    class Meta:
        model=Car
        fields="__all__"
#单个查询
@app.get("car/{car_id}",response=CarSchema)
def get_car_id(request,car_id:int):
    car=Car.objects.get(id=car_id)
    return car


#获取全部
@app.get("car",response=List[CarSchema])
def get_all(request): 
    car=Car.objects.all()
    return car

#添加数据
@app.post("car")
def c_car(request,car:CarSchema):
    car=Car.objects.create(**car.dict())
    return {"id":car.id}

#更新数据
@app.put("car/{car_id}")
def u_car(request,car_id:int,u_car:CarSchema):
    car=Car.objects.get(id=car_id)
    for attr,value in u_car.dict().items():
        setattr(car,attr,value)
    car.save()
        
    return {"id":car.id}

#删除数据
@app.delete("car/{car_id}")
def d_car(request,car_id:int): 
    car=Car.objects.get(id=car_id)
    car.delete()
    return HttpResponse("删除成功")


