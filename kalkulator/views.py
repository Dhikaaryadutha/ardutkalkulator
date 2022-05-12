from msilib.schema import SelfReg
from multiprocessing import context
from django import forms
from django.shortcuts import render
from numpy import integer
from .import forms
import numpy as np
from functools import reduce


def index(request):
	return render(request,'base.html')
#MATERI
def bangundatar(request):
	return render(request, 'bangundatar.html' )
def bangunruang(request):
    return render(request, 'bangunruang.html')
def pythagoras(request):
	return render(request,'pythagoras.html')
def panjang(request):
	if request.POST:
		sat_awal=request.POST.get('Satuan_awal')
		sat_akhir=request.POST.get('Satuan_akhir')
		nilai_awal=request.POST.get('Nilai_awal')
		nilaiawal=float(nilai_awal)
		satakhir=str(sat_akhir)
		if sat_awal==('KiloMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal/1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal/10,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal/100,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal/1000,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('HektoMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal*10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal*100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal*1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal*10,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*100,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('DekaMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal*10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal*100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal*1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*10,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('Meter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal*10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal*100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('DesiMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/10000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal*10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('CentiMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/100000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/10,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal/1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
		elif sat_awal==('MiliMeter'):
			if sat_akhir==('KiloMeter'):
				hasil=nilaiawal/1000,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('HektoMeter'):
				hasil=nilaiawal/100,000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DekaMeter'):
				hasil=nilaiawal/10000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('Meter'):
				hasil=nilaiawal/1000
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('DesiMeter'):
				hasil=nilaiawal/100
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('CentiMeter'):
				hasil=nilaiawal/10
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
			elif sat_akhir==('MiliMeter'):
				hasil=nilaiawal*1
				pesan="Panjangnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'panjang.html',konteks)
	else:
		a=forms.PanjangForm
		konteks={
			'a':a
		}
	return render(request,'panjang.html',konteks)

def berat(request):
	if request.POST:
		sat_awal=request.POST.get('Satuan_awal')
		sat_akhir=request.POST.get('Satuan_akhir')
		nilai_awal=request.POST.get('Nilai_awal')
		nilaiawal=float(nilai_awal)
		satakhir=str(sat_akhir)
		if sat_awal==('Ton'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah " 
				satuan=satakhir
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal*10
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal*1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal*10000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal*2205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*1000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*1000,000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('Kwintal'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/10
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal*100
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal*1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal*220.5
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*100,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*100,000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('KiloGram'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal/100
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal*10
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal*2.205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*1000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('Ons'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/10000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal/1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal/10
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal*0.2205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*10000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*100,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('Pon'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/2205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal/220.5
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal/2.205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal*2.205
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*453.5923
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*2205000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('Gram'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/1000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal/100,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal/1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal/10000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal/454
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
		elif sat_awal==('MiliGram'):
			if sat_akhir==('Ton'):
				hasil=nilaiawal/1000,000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Kwintal'):
				hasil=nilaiawal/100,000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('KiloGram'):
				hasil=nilaiawal/1000,000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Ons'):
				hasil=nilaiawal/1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Pon'):
				hasil=nilaiawal/453592
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('Gram'):
				hasil=nilaiawal/1000
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)
			elif sat_akhir==('MiliGram'):
				hasil=nilaiawal*1
				pesan="Beratnya adalah "
				satuan=satakhir 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satuan
				}
				return render(request,'berat.html',konteks)

	else:
		b=forms.BeratForm
		konteks={
			'b':b
		}
	return render(request, 'berat.html',konteks)
	
def kpk(request):
	return render(request, 'kpk.html')

#KPK&FPB

def duabilangan(request):
	if request.POST:
		bil_1=request.POST.get('bilangan_1')
		bil_2=request.POST.get('bilangan_2')
		bil1=int(bil_1)
		bil2=int(bil_2)
		kpk=np.lcm(bil1,bil2)
		fpb=np.gcd(bil1,bil2)
		pesan="KPK nya adalah "
		pesanfpb="FPB nya adalah "
		konteks={
			'kpk':kpk,
			'fpb':fpb,
			'pesanfpb':pesanfpb,
			'pesan':pesan
		}
		return render(request,'duabilangan.html',konteks)
	else:
		angka=forms.DuabilanganForm()

		konteks={
			'angka':angka,
		}
	return render(request,'duabilangan.html',konteks)
def tigabilangan(request):
	if request.POST:
		bil_1=request.POST.get('bilangan_1')
		bil_2=request.POST.get('bilangan_2')
		bil_3=request.POST.get('bilangan_3')

		bil1=int(bil_1)
		bil2=int(bil_2)
		bil3=int(bil_3)
		kpk=reduce(np.lcm,[bil1,bil2,bil3])
		fpb=reduce(np.gcd,[bil1,bil2,bil3])
		pesan="KPK nya adalah "
		pesanfpb="FPB nya adalah "
		konteks={
			'kpk':kpk,
			'fpb':fpb,
			'pesanfpb':pesanfpb,
			'pesan':pesan
		}
		return render(request,'tigabilangan.html',konteks)
	else:
		a=forms.TigabilanganForm()

		konteks={
			'a':a,
		}
	return render(request,'tigabilangan.html',konteks)
def empatbilangan(request):
	if request.POST:
		bil_1=request.POST.get('bilangan_1')
		bil_2=request.POST.get('bilangan_2')
		bil_3=request.POST.get('bilangan_3')
		bil_4=request.POST.get('bilangan_4')

		bil1=int(bil_1)
		bil2=int(bil_2)
		bil3=int(bil_3)
		bil4=int(bil_4)

		kpk=reduce(np.lcm,[bil1,bil2,bil3,bil4])
		fpb=reduce(np.gcd,[bil1,bil2,bil3,bil4])
		pesan="KPK nya adalah "
		pesanfpb="FPB nya adalah "
		konteks={
			'kpk':kpk,
			'fpb':fpb,
			'pesanfpb':pesanfpb,
			'pesan':pesan
		}
		return render(request,'empatbilangan.html',konteks)
	else:
		a=forms.EmpatbilanganForm()

		konteks={
			'a':a,
		}
	return render(request,'empatbilangan.html',konteks)

def suhu(request):
	if request.POST:
		sat_awal=request.POST.get('Satuan_awal')
		sat_akhir=request.POST.get('Satuan_akhir')
		nilai_awal=request.POST.get('Nilai_awal')
		nilaiawal=int(nilai_awal)
		satakhir=str(sat_akhir)
		if sat_awal==('Celcius'):
			if sat_akhir==('Celcius'):
				hasil=nilaiawal*1
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Reamur'):
				hasil=nilaiawal*(4/5)
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Fahrenheit'):
				hasil=(9/5) * nilaiawal + 32
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Rankine'):
				hasil=(nilaiawal+273.15)*1.8
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Kelvin'):
				hasil=nilaiawal+273.15
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
		if sat_awal==('Reamur'):
			if sat_akhir==('Reamur'):
				hasil=nilaiawal*1
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Celcius'):
				hasil=(5/4)*nilaiawal
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Fahrenheit'):
				hasil=(9/4*nilaiawal)+32
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Rankine'):
				hasil=nilaiawal*2.25+491.67
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Kelvin'):
				hasil=nilaiawal/0.8+273.15
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
		if sat_awal==('Fahrenheit'):
			if sat_akhir==('Fahrenheit'):
				hasil=nilaiawal*1
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Celcius'):
				hasil=(nilaiawal-32)*(5/9)
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Reamur'):
				hasil=(4/9)*(nilaiawal-32)
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Rankine'):
				hasil=nilaiawal+459.67
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Kelvin'):
				hasil=(nilaiawal-32)*(5/9)+273.15
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
		if sat_awal==('Rankine'):
			if sat_akhir==('Rankine'):
				hasil=nilaiawal*1
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Celcius'):
				hasil=(nilaiawal/1.8)-273.15
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Reamur'):
				hasil=(nilaiawal/1.8+273.15)*0.8
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Fahrenheit'):
				hasil=nilaiawal-459.67
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Kelvin'):
				hasil=nilaiawal/1.8
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
		if sat_awal==('Kelvin'):
			if sat_akhir==('Kelvin'):
				hasil=nilaiawal*1
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Celcius'):
				hasil=nilaiawal-273.15
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Reamur'):
				hasil=(nilaiawal-273.15)*0.8
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Rankine'):
				hasil=nilaiawal*1.8
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
			elif sat_akhir==('Fahrenheit'):
				hasil=nilaiawal*1.8-459.67
				pesan="Suhunya adalah " 
				konteks={
					'hasil':hasil,
			        'pesan':pesan,
					'satuan':satakhir
				}
				return render(request,'suhu.html',konteks)
	else:
		suhu=forms.SuhuForm()
		konteks={
		    'suhu':suhu
	    }
		return render(request,'suhu.html',konteks)

#Pythagoras	
def sisia(request):
	if request.POST:
		sisib=request.POST.get('Sisib')
		sisic=request.POST.get('Sisic')
		sisi_b=int(sisib)
		sisi_c=int(sisic)

		sisi_a= (sisi_c**2-sisi_b**2)**0.5
		pesan="Panjang sisi a adalah " 
            
		konteks={
			'sisi_a':sisi_a,
			'pesan':pesan
		}
		return render(request,'sisia.html',konteks)
	else:
		sisi_a=forms.SisiaForm()

		konteks={
			'sisi_a':sisi_a,
		}
	return render(request,'sisia.html',konteks)

def sisib(request):
	if request.POST:
		sisia=request.POST.get('Sisia')
		sisic=request.POST.get('Sisic')
		sisi_a=int(sisia)
		sisi_c=int(sisic)

		sisi_b= (sisi_c**2-sisi_a**2)**0.5
		pesan="Panjang sisi b adalah " 
            
		konteks={
			'sisi_b':sisi_b,
			'pesan':pesan
		}
		return render(request,'sisib.html',konteks)
	else:
		sisi_b=forms.SisibForm()

		konteks={
			'sisi_b':sisi_b,
		}
	return render(request,'sisib.html',konteks)
def sisic(request):
	if request.POST:
		sisia=request.POST.get('Sisia')
		sisib=request.POST.get('Sisib')
		sisi_a=int(sisia)
		sisi_b=int(sisib)

		sisi_c= (sisi_b**2+sisi_a**2)**0.5
		pesan="Panjang sisi c adalah " 
            
		konteks={
			'sisi_c':sisi_c,
			'pesan':pesan
		}
		return render(request,'sisic.html',konteks)
	else:
		sisi_c=forms.SisicForm()

		konteks={
			'sisi_c':sisi_c,
		}
	return render(request,'sisic.html',konteks)

#BANGUNDATAR
def persegi(request):
	if request.POST:
		sisi_persegi=request.POST.get('Sisi')
		sisipersegi=int(sisi_persegi)
		luaspersegi=sisipersegi**2
		kelilingpersegi=sisipersegi*4
		pesanluas="Luasnya adalah " 
		pesankeliling="Kelilingnya adalah "
            
		konteks={
			'luaspersegi':luaspersegi,
			'kelilingpersegi':kelilingpersegi,
			'pesanluas':pesanluas,
			'pesankeliling':pesankeliling
		}
		return render(request,'persegi.html',konteks)
	else:
		sisipersegi=forms.PersegiForm()

		konteks={
			'sisipersegi':sisipersegi,
		}
		
	return render(request, 'persegi.html',konteks)

def persegipanjang1(request):
	if request.POST:
		panjangpp=request.POST.get('Panjang')
		lebarpp=request.POST.get('Lebar')
		lebar_pp=int(lebarpp)
		panjang_pp=int(panjangpp)

		luas_pp=panjang_pp*lebar_pp
		kl_pp=(panjang_pp+lebar_pp)*2
		pesanls="Luasnya adalah " 
		pesankl="Kelilingnya adalah "
            
		konteks={
			'luas_pp':luas_pp,
			'kl_pp':kl_pp,
			'pesan':pesanls,
			'pesankl':pesankl
		}
		return render(request,'persegipanjang.html',konteks)
	else:
		sisi_pp=forms.PersegipanjangForm()

		konteks={
			'sisi_pp':sisi_pp,
		}
	return render(request, 'persegipanjang.html',konteks)
def segitiga(request):
	if request.POST:
		tinggisegitiga=request.POST.get('Tinggi')
		alassegitiga=request.POST.get('Alas')
		tinggi_segitiga=int(tinggisegitiga)
		alas_segitiga=int(alassegitiga)

		luas_segitiga=(tinggi_segitiga*alas_segitiga)/2

		pesan="Luasnya adalah " 
            
		konteks={
			'luas_segitiga':luas_segitiga,
			'pesan':pesan
		}
		return render(request,'segitiga.html',konteks)
	else:
		sisi_segitiga=forms.SegitigaForm()

		konteks={
			'sisi_segitiga':sisi_segitiga,
		}
	return render(request, 'segitiga.html',konteks)
def lingkaran(request):
	if request.POST:
		jj_lingkaran=request.POST.get('Jarijari')
		jjlingkaran=int(jj_lingkaran)
		if jjlingkaran%7==0:
			phi=22/7
		else:
			phi=3.14
		luas_lingkaran=phi*jjlingkaran**2
		kl_lingkaran=2*phi*jjlingkaran
		pesan="Luasnya adalah " 
		pesankl="Kelilingnya adalah "
            
		konteks={
			'luas_lingkaran':luas_lingkaran,
			'kl_lingkaran':kl_lingkaran,
			'pesankl':pesankl,
			'pesan':pesan
		}
		return render(request,'lingkaran.html',konteks)
	else:
		jj_lingkaran=forms.LingkaranForm()

		konteks={
			'jj_lingkaran':jj_lingkaran,
		}
	return render(request, 'lingkaran.html',konteks)
def jajargenjang(request):
	if request.POST:
		alas_jjr=request.POST.get('Alas')
		tinggi_jjr=request.POST.get('Tinggi')

		alasjjr=int(alas_jjr)
		tinggijjr=int(tinggi_jjr)

		luas_jjr=alasjjr*tinggijjr
		pesan="Luasnya adalah " 
            
		konteks={
			'luas_jjr':luas_jjr,
			'pesan':pesan
		}
		return render(request,'jajargenjang.html',konteks)
	else:
		sisi_jajargenjang=forms.JajargenjangForm()

		konteks={
			'sisi_jjr':sisi_jajargenjang,
		}
	return render(request,'jajargenjang.html',konteks)

def trapesium(request):
	if request.POST:
		sisi_a=request.POST.get('Sisia')
		sisi_b=request.POST.get('Sisib')
		tinggi=request.POST.get('Tinggi')

		sisia=int(sisi_a)
		sisib=int(sisi_b)
		Tinggi=int(tinggi)

		luas_trapesium=1/2*(sisia+sisib)*Tinggi
		pesan="Luasnya adalah " 
            
		konteks={
			'luas_trapesium':luas_trapesium,
			'pesan':pesan
		}
		return render(request,'trapesium.html',konteks)
	else:
		sisi_trapesium=forms.TrapesiumForm()

		konteks={
			'sisi_trapesium':sisi_trapesium,
		}
	return render(request,'trapesium.html',konteks)

def belahketupat(request):
	if request.POST:
		diagonal1=request.POST.get('Diagonal_1')
		diagonal2=request.POST.get('Diagonal_2')

		diagonal_1=int(diagonal1)
		diagonal_2=int(diagonal2)

		luas_belahketupat=1/2*diagonal_1*diagonal_2
		pesan="Luasnya adalah " 
            
		konteks={
			'luas_belahketupat':luas_belahketupat,
			'pesan':pesan
		}
		return render(request,'belahketupat.html',konteks)
	else:
		sisi_belahketupat=forms.BelahketupatForm()

		konteks={
			'sisi_belahketupat':sisi_belahketupat,
		}

	return render(request,'belahketupat.html',konteks)

def layanglayang(request):
	if request.POST:
		diagonal1=request.POST.get('Diagonal_1')
		diagonal2=request.POST.get('Diagonal_2')

		diagonal_1=int(diagonal1)
		diagonal_2=int(diagonal2)

		luas_layanglayang=1/2*diagonal_1*diagonal_2
		pesan="Luasnya adalah " 
            
		konteks={
			'luas_layanglayang':luas_layanglayang,
			'pesan':pesan
		}
		return render(request,'layanglayang.html',konteks)
	else:
		sisi_layanglayang=forms.LayanglayangForm()

		konteks={
			'sisi_layanglayang':sisi_layanglayang,
		}

	return render(request,'layanglayang.html',konteks)
#BANGUNRUANG
def kubus(request):
	if request.POST:
		sisi_kubus=request.POST.get('Sisi')

		volume_kubus=int(sisi_kubus)**3
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_kubus':volume_kubus,
			'pesan':pesan
		}
		return render(request,'kubus.html',konteks)
	else:
		sisi_kubus=forms.KubusForm()

		konteks={
			'sisi_kubus':sisi_kubus,
		}
	return render(request, 'kubus.html',konteks)
def balok(request):
	if request.POST:
		panjang_balok=request.POST.get('Panjang')
		lebar_balok=request.POST.get('Lebar')
		tinggi_balok=request.POST.get('Tinggi')

		volume_balok=int(panjang_balok)*int(lebar_balok)*int(tinggi_balok)
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_balok':volume_balok,
			'pesan':pesan
		}
		return render(request,'balok.html',konteks)
	else:
		sisi_balok=forms.BalokForm()

		konteks={
			'sisi_balok':sisi_balok,
		}
	return render(request, 'balok.html',konteks)
def kerucut(request):
	if request.POST:
		jj_kerucut=request.POST.get('Jarijari')
		tinggi_kerucut=request.POST.get('Tinggi')
		
		tinggikerucut=int(tinggi_kerucut)
		jjkerucut=int(jj_kerucut)
		if jjkerucut%7==0:
			phi=22/7
		else:
			phi=3.14
		volume_kerucut=(1/3)*phi*jjkerucut**2*tinggikerucut
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_kerucut':volume_kerucut,
			'pesan':pesan
		}
		return render(request,'kerucut.html',konteks)
	else:
		jj_kerucut=forms.KerucutForm()

		konteks={
			'jj_kerucut':jj_kerucut,
		}
	return render(request, 'kerucut.html',konteks)
def bola(request):
	if request.POST:
		jj_bola=request.POST.get('Jarijari')
		jjbola=int(jj_bola)
		if jjbola%7==0:
			phi=22/7
		else:
			phi=3.14
		luas_bola=(4/3)*phi*jjbola**3
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_bola':luas_bola,
			'pesan':pesan
		}
		return render(request,'bola.html',konteks)
	else:
		jj_bola=forms.LingkaranForm()

		konteks={
			'jj_bola':jj_bola,
		}
	return render(request, 'bola.html',konteks)

def tabung(request):
	if request.POST:
		jj_tabung=request.POST.get('Jarijari')
		tinggi_tabung=request.POST.get('Tinggi')
		
		tinggitabung=int(tinggi_tabung)
		jjtabung=int(jj_tabung)
		if jjtabung%7==0:
			phi=22/7
		else:
			phi=3.14
		volume_tabung=phi*jjtabung**2*tinggitabung
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_tabung':volume_tabung,
			'pesan':pesan
		}
		return render(request,'tabung.html',konteks)
	else:
		jj_tabung=forms.TabungForm()

		konteks={
			'jj_tabung':jj_tabung,
		}

	return render(request,'tabung.html',konteks)

def prismasegi3(request):
	if request.POST:
		aa=request.POST.get('a')
		tt=request.POST.get('t')
		tinggi=request.POST.get('Tinggi')
		
		a=int(aa)
		t=int(tt)
		Tinggi=int(tinggi)

		volume_prisma=(a*t/2)*Tinggi
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_prisma':volume_prisma,
			'pesan':pesan
		}
		return render(request,'prismasegitiga.html',konteks)
	else:
		sisi_prisma=forms.PrismasegitigaForm()

		konteks={
			'sisi_prisma':sisi_prisma,
		}
	return render(request,'prismasegitiga.html',konteks)

def limassegi4(request):
	if request.POST:
		pa=request.POST.get('P_alas')
		la=request.POST.get('L_alas')
		tinggi=request.POST.get('Tinggi')
		
		a=int(pa)
		t=int(la)
		Tinggi=int(tinggi)

		volume_limas=1/3*(a*t)*Tinggi
		pesan="Volumenya adalah " 
            
		konteks={
			'volume_limas':volume_limas,
			'pesan':pesan
		}
		return render(request,'limassegi4.html',konteks)
	else:
		sisi_limas=forms.Limassegi4Form()

		konteks={
			'sisi_limas':sisi_limas,
		}
	return render(request,'limassegi4.html',konteks)