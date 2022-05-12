from django import forms
#PHYTAGORAS
class SisiaForm(forms.Form):
    Sisib=forms.FloatField()
    Sisic=forms.FloatField()

class SisibForm(forms.Form):
    Sisia=forms.FloatField()
    Sisic=forms.FloatField()

class SisicForm(forms.Form):
    Sisia=forms.FloatField()
    Sisib=forms.FloatField()

#BANGUN DATAR

class PersegiForm(forms.Form):
    Sisi=forms.FloatField()

class PersegipanjangForm(forms.Form):
    Panjang=forms.FloatField()
    Lebar=forms.FloatField()

class SegitigaForm(forms.Form):
    Alas=forms.FloatField()
    Tinggi=forms.FloatField()

class LingkaranForm(forms.Form):
    Jarijari=forms.FloatField()

class JajargenjangForm(forms.Form):
    Alas=forms.FloatField()
    Tinggi=forms.FloatField()

class TrapesiumForm(forms.Form):
    Sisia=forms.FloatField()
    Sisib=forms.FloatField()
    Tinggi=forms.FloatField()

class LayanglayangForm(forms.Form):
    Diagonal_1=forms.FloatField()
    Diagonal_2=forms.FloatField()

class BelahketupatForm(forms.Form):
    Diagonal_1=forms.FloatField()
    Diagonal_2=forms.FloatField()



#BANGUN RUANG

class KubusForm(forms.Form):
    Sisi=forms.FloatField()

class BalokForm(forms.Form):
    Panjang=forms.FloatField()
    Lebar=forms.FloatField()
    Tinggi=forms.FloatField()

class KerucutForm(forms.Form):
    Jarijari=forms.FloatField()
    Tinggi=forms.FloatField()

class BolaForm(forms.Form):
    Jarijari=forms.FloatField()

class TabungForm(forms.Form):
    Jarijari=forms.FloatField()
    Tinggi=forms.FloatField()

class PrismasegitigaForm(forms.Form):
    a=forms.FloatField()
    t=forms.FloatField()
    Tinggi=forms.FloatField()

class Limassegi4Form(forms.Form):
    P_alas=forms.FloatField()
    L_alas=forms.FloatField()
    Tinggi=forms.FloatField()

#PANJANG
class PanjangForm(forms.Form):
    chs=[
        ('KiloMeter','KiloMeter'),
        ('HektoMeter','HektoMeter'),
        ('DekaMeter','DekaMeter'),
        ('Meter','Meter'),
        ('DesiMeter','DesiMeter'),
        ('CentiMeter','CentiMeter'),
        ('MiliMeter','MiliMeter'),
        
    ]
    Satuan_awal=forms.ChoiceField(choices=chs)
    Nilai_awal=forms.FloatField()
    Satuan_akhir=forms.ChoiceField(choices=chs)

#BERAT
class BeratForm(forms.Form):
    chs=[
        ('Ton','Ton'),
        ('Kwintal','Kwintal'),
        ('KiloGram','KiloGram'),
        ('Ons','Ons'),
        ('Pon','Pon'),
        ('Gram','Gram'),
        ('MiliGram','MiliGram'),
        
    ]
    Satuan_awal=forms.ChoiceField(choices=chs)
    Nilai_awal=forms.FloatField()
    Satuan_akhir=forms.ChoiceField(choices=chs)

class DuabilanganForm(forms.Form):
    bilangan_1=forms.FloatField()
    bilangan_2=forms.FloatField()
class TigabilanganForm(forms.Form):
    bilangan_1=forms.FloatField()
    bilangan_2=forms.FloatField()
    bilangan_3=forms.FloatField()
class EmpatbilanganForm(forms.Form):
    bilangan_1=forms.FloatField()
    bilangan_2=forms.FloatField()
    bilangan_3=forms.FloatField()
    bilangan_4=forms.FloatField()

#SUHU

class SuhuForm(forms.Form):
    chs=[
        ('Celcius','Celcius °C'),
        ('Fahrenheit','Fahrenheit °F'),
        ('Reamur',' Reamur °Re'),
        ('Rankine','Rankine °R'),
        ('Kelvin','Kelvin K'),
    ]
    Satuan_awal=forms.ChoiceField(choices=chs)
    Nilai_awal=forms.FloatField()
    Satuan_akhir=forms.ChoiceField(choices=chs)

    