 #Girilen TC kimlik numarasının dogruluğunun sorgulanması

 #Copyright (C) <2016>  <Hazal KAYA>

   # This program is free software: you can redistribute it and/or modify
   # it under the terms of the GNU General Public License as published by
   # the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.

   # This program is distributed in the hope that it will be useful,
   # but WITHOUT ANY WARRANTY; without even the implied warranty of
   # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   # GNU General Public License for more details.

   # You should have received a copy of the GNU General Public License
   # along with this program.  If not, see <http://www.gnu.org/licenses/>. 


def TCAlgoritma(TCno):
    if(len(TCno)!= 11) or (int(TCno[0]) == 0):
        print("Geçersiz değer girdiniz, tekrar deneyiniz!")
    else:
        t1=t2=0 #t1 tek basamaktaki,t2 cift basamaktaki değerler
        sayac=0
        while sayac<8:
            t1+=int(TCno[sayac])
            t2+=int(TCno[sayac+1])
            sayac+=2
        t1 += int(TCno[8])
        onuncu_b = (t1 * 7 - t2) % 10 
        onbirinci_b = (t1 + t2 + onuncu_b) % 10
        if(int(TCno[9]) == onuncu_b) and (int(TCno[10]) == onbirinci_b):
            print("Gecerli TC kimlik numarasi girilmiştir!")
        else:
            print("Gecersiz TC kimlik numarası girilmiştir!")

print('#'*30)
print("Copyright (C) <2016>  <Hazal KAYA>")
print('#'*30)
no= input("""TC kimlik no giriniz
Cıkmak icin q'ya basınız!
""")
if(no != 'q'):
    TCAlgoritma(no)
else:
    exit()

