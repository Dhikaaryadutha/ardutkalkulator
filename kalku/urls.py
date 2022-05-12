from django.conf.urls import url
from django.contrib import admin
from kalkulator.views import index, bangundatar,bangunruang,pythagoras,panjang,berat,kpk,suhu,duabilangan,tigabilangan,empatbilangan,sisia,sisib,sisic,persegi,persegipanjang1,segitiga,lingkaran,jajargenjang,trapesium,layanglayang,belahketupat,kubus,balok,kerucut,bola,tabung,prismasegi3,limassegi4

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', index),
    #MATERI
    url('bangundatar/', bangundatar),
    url('bangunruang/', bangunruang),
    url('pythagoras/', pythagoras),
    url('panjang/', panjang),
    url('berat/', berat),
    url('kpk/', kpk),
    url('suhu/',suhu),
    #KPK&FPB
    url('duabilangan/',duabilangan),
    url('tigabilangan/',tigabilangan),
    url('empatbilangan/',empatbilangan),

    #PHYTAGORAS
    url('sisia/', sisia),
    url('sisib/', sisib),
    url('sisic/', sisic),
    #BANGUN DATAR
    url('persegi/', persegi),
    url('persegipanjang1/', persegipanjang1),
    url('segitiga/', segitiga),
    url('lingkaran/', lingkaran),
    url('jajargenjang/', jajargenjang),
    url('trapesium/', trapesium),
    url('belahketupat/', belahketupat),
    url('layanglayang/', layanglayang),
    #BANGUN RUANG
    url('kubus/', kubus),
    url('balok/', balok),
    url('kerucut/', kerucut),
    url('bola/', bola),
    url('tabung/', tabung),
    url('prismasegi3/', prismasegi3),
    url('limassegi4/', limassegi4),

]