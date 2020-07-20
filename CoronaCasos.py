# -*- coding: utf-8 -*-

# Este programa es de software libre; Pude redistribuirlo así como modificarlo de acuerdo con las políticas respectivas. 
# Este programa es distribuido con la esperanza de que sea útil. Sin embargo, no hay GARANTÍA EXISTENTE.
# Cualquier contribución es bienvenida
# Información de licencia:
#This is free and unencumbered software released into the public domain.
#
#Anyone is free to copy, modify, publish, use, compile, sell, or
#distribute this software, either in source code form or as a compiled
#binary, for any purpose, commercial or non-commercial, and by any
#means.
#
#In jurisdictions that recognize copyright laws, the author or authors
#of this software dedicate any and all copyright interest in the
#software to the public domain. We make this dedication for the benefit
#of the public at large and to the detriment of our heirs and
#successors. We intend this dedication to be an overt act of
#relinquishment in perpetuity of all present and future rights to this
#software under copyright law.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#
#For more information, please refer to <https://unlicense.org>

___author___ = "Juan Felipe Rubiano"
___license___ = "Public Domain"
___version___ = "1.0"


from covid import Covid
import time
import sys
import os
import subprocess
#Algunas librerías solo están para pruebas o elementos temporalmente desactivados



#=====================================================================
#ANTES DE CUALQUIER COSA, PORFAVOR LEER EL README.md
#=====================================

# Requerimientos: Python >= 3.6
# Instalar librería covid: pip install covid

#Link del repositorio: https://github.com/Juan-Felipe-Rubiano/Casos-de-Coronavirus.git

#Pruebas para modificar tamaño de consola
#os.system('mode con: cols=10 lines=42')
#subprocess.Popen(["mode", "con:", "cols=25", "lines=80"])
#cmd = 'mode 20,20'
#os.system(cmd)




#Orden del programa: Inicio-Desarrollo-Final-Pregunta(Todo está separado en funciones y juntado en "programaCompleto") 

def programaInicio():
    covid = Covid()
    paises = covid.list_countries()
    print("""Bienvenido a CoronaCasos!
    
    Esta es la lista de paises:\n""")
    #print(paises)
    #Lista de países disponibles para consulta
    print("""
    -US             -Chile          -Brazil         -United Kingdom     -Luxembourg              
    -India          -Iran           -Russia         -Pakistan           -Antigua and Barbuda     
    -South Africa   -Spain          -Peru           -Saudi Arabia       -Sri Lanka               
    -Mexico         -Italy          -Turkey         -France             -Jamaica                 
    -Bangladesh     -Germany        -Colombia       -Argentina          -Belize                  
    -Canada         -Qatar          -Iraq           -Egypt              -Bahamas                 
    -Indonesia      -China          -Sweden         -Ecuador            -Togo
    -Kazakhstan     -Philippines    -Oman           -Belarus            -Djibouti
    -Belgium        -Ukraine        -Kuwait         -Bolivia            -Saint Vicent and the Grenadines
    -Panama         -Netherlands    -Israel         -Portugal           -Congo (Brazzaville)
    -Singapore      -Poland         -Romania        -Nigeria            -Trinidad and Tobago
    -Bahrain        -Afghanistan    -Armenia        -Guatemala          -Congo (Kinshasa)   
    -Switzerland    -Honduras       -Azerbaijan     -Ghana              -Equatorial Guinea
    -Ireland        -Japan          -Kyrgyzstan     -Algeria            -MS Zaandam
    -Moldova        -Serbia         -Austria        -Austria            -Papua New Guinea
    -Nepal          -Morocco        -Uzbekistan     -Cameroon           -Saint Kitts and Nevis
    -Cote d'Ivoire  -Czechia        -Korea          -Denmark            -Sao Tome and Principe
    -Kenya          -El Salvador    -Australia      -Venezuela          -Diamond Princess
    -Sudan          -Costa Rica     -Ethiopia       -North Macedonia    -United Arab Emirates
    -Norway         -Senegal        -Malaysia       -Bulgaria           -Central African Republic
    -Finland        -Haiti          -Madagascar     -Tajikistan         -Dominican Republic
    -Guinea         -Gabon          -Mauritania     -Kosovo             -West Bank and Gaza
    -Croatia        -Hungary        -Albania        -Greece             -Bosnia and Herzegovina
    -Paraguay       -Thailand       -Nicaragua      -Somalia            -Dominica
    -Zambia         -Maldives       -Malawi         -Lebanon            -Laos 
    -Mali           -Cuba           -South Sudan    -Montenegro         -Saint Lucia
    -Cabo Verde     -Estonia        -Slovakia       -Guinea-Bissau      -Grenada
    -Slovenia       -Lithuania      -Iceland        -Libya              -Western Sahara
    -Eswatini       -Sierra Leone   -Yemen          -Benin              -Holy See
    -New Zealand    -Rwanda         -Mozambique     -Zimbabwe           -Timor-Leste
    -Tunisia        -Suriname       -Chad           -Andorra            -Fiji
    -San Marino     -Angola         -Malta          -Botswana           -Gambia
    -Tanzania       -Syria          -Taiwan         -Vietnam            -Barbados
    -Lesotho        -Mauritius      -Burma          -Comoros            -Seychelles        
    -Guyana         -Burundi        -Mongolia       -Eritrea            -Monaco
    -Cambodia       -Brunei         -Bhutan         -Liechtensten
    """)
    print("""
    ===========================================================================================
    ===========================================================================================""")
    
def programaDesarrollo():
    covid = Covid()
    eleccion = input("Escribe el nombre del país que desees:\t")
    cases = covid.get_status_by_country_name(eleccion)
    print("\n \n \n \n \n")
    for i in cases:
	    print(i, ":", cases[i])

def programaFinal():
    time.sleep(4)
    print("Fuente de datos: John Hopkins University")


correr = 1 #Variable para usar en la función pregunta y programaCompleto. Correr = ejecutar(programa)

def pregunta():
    while correr == 1:
        continuar = input("Continuar?(s/n) ")
        if continuar in ("Yes", "YES", "yes", "Y", "y", "si", "SI", "s", "S", "Sí", "Sí", "sí", "Si")or not continuar:
            programaCompleto()
        else:
            print("Saliendo...")
            sys.exit()

def programaCompleto():
    programaInicio()
    programaDesarrollo()
    programaFinal()
    pregunta()
    



while correr == 1:
    programaCompleto()




#input() (para pruebas)