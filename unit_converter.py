#--------------------- instagram ----------------------#

#--------------------- the_kira_x ---------------------#



#---------------------- imports -----------------------#

from colorama import Fore,Back,init,Style
import subprocess
import time
init(autoreset=True)

#----------------------- end --------------------------#


#----------------------- DATA -------------------------#

type=['Length','Weight','Volume','Data Conversion',
'Temperature','Time','Days','Exit']

l=['Metre to Kilometre','Kilometre to Metre',
'Metre to Centimetre','Centimetre to Metre',
'Centimetre to Milimetre','Milimetre to Centimetre',
'Inch to Centimetre','Centimetre to Inch','Foot to Metre',
'Metre to Foot','Mile to Kilometre','Kilometre to Mile',
'Exit']

w=['Gram to Kilogram','Kilogram to Gram',
'Gram to Miligram','Miligram to Gram',
'kilogram to Pound (lbs)','Pound (lbs) to Kilogram']

v=['Milimetre to Litre','Litre to Milimetre',
'Gallon (US) to Litre','Litre to Gallon (US)','Exit']

d=['Kilobyte (KB) to Megabite (MB)',
'Megabyte (MB) to Kilobyte (KB)',
'Megabyte (MB) to Gigabyte (GB)',
'Gigabyte (GB) to Megabit (MB)',
'Gigabyte (GB) to Terabyte (TB)',
'Terabyte (TB) to Gigabyte (GB)','Exit']

t=['Celsius to Fahrenheit','Fahrenheit to Celsius',
'Celsius to Kelvin','Kelvin to Celsius','Exit']

T=['Seconds to Minutes','Minutes to Seconds',
'Minutes to Hours','Hours to Minutes',
'Hours to Days','Days to Hours','Exit']

D=['Days to Weeks','Weeks to Days',
'Days to Months','Months to Days',
'Days to Years','Years to Days','Exit']

#------------------------ end -------------------------#



#---------------------- starting ----------------------#

def loading():
    for i in range (0,10):
        print(Style.BRIGHT+Fore.YELLOW+"*"*i)
        time.sleep(0.5)
loading()
subprocess.run(["clear"])
print("\n")
count=0
for items in type:
    count+=1
    print(Style.BRIGHT+Fore.CYAN+f"{count} {items}{"\n"}")

type_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose your option (1/2/3/4/5/6/7/8) :"))
init(autoreset=True)

#------------------------ end -------------------------#



#------------------- Length Function ------------------#

if type_choose == 1:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in l:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    l_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if l_choose == 1:
        def m_to_km(m):
            return metre_input/1000
        metre_input=float(input(f"enter your metre quantity:"))
        result=m_to_km(metre_input)
        print(f"{metre_input} metre is equal to {result:.1F} km")

    elif l_choose == 2:
        def km_to_m(km):
            return km_input*1000
        km_input=float(input("enter your km quantity:"))
        result=km_to_m(km_input)
        print(f"{km_input} metre is equal to {round} {result:.1F} metres")

    elif l_choose == 3:
        def m_to_cm(m):
            return metre*100
        metre=float(input("enter your metre quantity:"))
        result=m_to_cm(metre)
        print(f"{metre} metre is equal to {result:.1F} cm")

    elif l_choose == 4:
        def cm_to_m(cm):
            return cm_input/100
        cm_input=float(input("enter your centimetre quantity:"))
        result=cm_to_m(cm_input)
        print(f"{cm_input} metre is equal to {result:.1F} metre")


    elif l_choose == 5:
        def cm_to_mm(cm):
            return cm*10
        cm=float(input("enter your cm quantity:"))
        result=cm_to_mm(cm)
        print(f"{cm} metre is equal to {result:.1F} mm")

    elif l_choose == 6:
        def mm_to_cm(mm):
            return mm_input/10
        mm_input=float(input("enter your mm quantity:"))
        result=mm_to_cm(mm_input)
        print(f"{mm_input} mm is equal to {result:.1F} cm")

    elif l_choose == 7:
        def inch_to_cm(inch ):
            return inch_input*2.54
        inch_input=float(input("enter your inch quantity:"))
        result=inch_to_cm(inch_input)
        print(f"{inch_input} inch is equal to {result:.1F} cm")

    elif l_choose == 8:
        def cm_to_inch(cm):
            return cm_01_input/2.54
        cm_01_input=float(input("enter your cm quantity:"))
        result=cm_to_inch(cm_01_input)
        print(f"{cm_01_input} inch is equal to {result:.1F} inch")

    elif l_choose == 9:
        def ft_to_m(ft):
            return ft_input*0.3048
        ft_input=float(input("enter your ft quantity:"))
        result=ft_to_m(ft_input)
        print(f"{ft_input} ft is equal to {result:.1F} metre")

    elif l_choose == 10:
        def m_to_ft(m):
            return m_01_input/0.3048
        m_01_input=float(input("enter your metre quantity:"))
        result=m_to_ft(m_01_input)
        print(f"{m_01_input} metre is equal to {result:.1F} ft")

    elif l_choose == 11:
        def mile_to_km(mile):
            return mile_input*1.60934
        mile_input=float(input("enter your mile quantity:"))
        result=mile_to_km(mile_input)
        print(f"{mile_input} mile is equal to {result:.1F} km")

    elif l_choose == 12:
        def km_to_mile(km):
            return km/1.60934
        km=float(input("enter your km quantity:"))
        result=km_to_mile(km)
        print(f"{km} km is equal to {result:.1F} mile")
    else:
        print("something went wrong in length function")

#------------------------ end -------------------------#



#------------------ weight function -------------------#

elif type_choose == 2:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in w:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    w_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if w_choose == 1:
        def g_to_kg(g):
            return g/1000
        g=float(input("enter your gram quantity:"))
        result=g_to_kg(g)
        print(f"{g} is equal to {result:.1F} kg")

    elif w_choose == 2:
        def kg_to_g(kg):
            return kg*1000
        kg=float(input("enter your kg quantity:"))
        result=kg_to_g(kg)
        print(f"{kg} is equal to {result:.1F} g")

    elif w_choose == 3:
        def gram_to_miligram(gram):
            return gram*1000
        gram=float(input("enter your gram quantity:"))
        result=gram_to_miligram(gram)
        print(f"{gram} is equal to {result:.1F} miligram")

    elif w_choose == 4:
        def miligram_to_g(miligram):
            return miligram/1000
        miligram=float(input("enter your miligram quantity:"))
        result=miligram_to_g(miligram)
        print(f"{miligram} is equal to {result:.1F} gram")

    elif w_choose == 5:
        def kilogram_to_pound(kilogram):
            return kilogram*2.20462
        kilogram=float(input("enter your kilogram quantity:"))
        result=kilogram_to_pound(kilogram)
        print(f"{kilogram} is equal to {result:.1F} pound(lbs)")

    elif w_choose == 6:
        def pound_to_kg(pound):
            return pound/2.20462
        pound=float(input("enter your pound quantity:"))
        result=pound_to_kg(pound)
        print(f"{pound}lbs is equal to {result:.1f} kg")

    else:
        print("something went wrong in weight function")

#------------------------- end ------------------------#



#------------------- volume function ------------------#

elif type_choose == 3:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in v:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    v_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if v_choose == 1:
        def mm_to_litre(mm):
            return mm/1000
        mm=float(input("enter volume in mm:"))
        result=mm_to_litre(mm)
        print(f"{mm} is equal to {result:.1F} litres")

    elif v_choose == 2:
        def litre_to_milimetre(litre):
            return litre*1000
        litre=float(input("enter volume in litres:"))
        result=litre_to_milimetre(litre)
        print(f"{litre} is equal to {result:.1F} milimitres")

    elif v_choose == 3:
        def gallon_to_litre(gallon):
            return gallon*3.78541
        gallon=float(input("enter volume in gallon:"))
        result=gallon_to_litre(gallon)
        print(f"{gallon} is equal to {result:.1F} litres")

    elif v_choose == 4:
        def litre_to_gallon(litre):
            return litre/3.78541
        litre=float(input("enter volume in litres:"))
        result=litre_to_gallon(litre)
        print(f"{litre} is equal to {result:.1F} gallon")

    else:
        print("something went wrong in volume function")

#------------------------ end ------------------------#



#------------------- data function -------------------#

elif type_choose == 4:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in d:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")    
    d_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if d_choose == 1:
        def kb_to_mb(kb):
            return kb/1000
        kb=float(input("enter data value in kb:"))
        result=kb_to_mb(kb)
        print(f"{kb} kb is equal to {result:.1F} mb")

    elif d_choose == 2:
        def mb_to_kb(mb):
            return mb*1000
        mb=float(input("enter data value in mb:"))
        result=mb_to_kb(mb)
        print(f"{mb} mb is equal to {result:.1F} kb")

    elif d_choose == 3:
        def mb_to_gb(mb):
            return mb/1000
        mb=float(input("enter data value in mb:"))
        result=mb_to_gb(mb)
        print(f"{mb} mb is equal to {result:.1F} gb")

    elif d_choose == 4:
        def gb_to_mb(gb):
            return gb*1000
        gb=float(input("enter data value in gb:"))
        result=gb_to_mb(gb)
        print(f"{gb} gb is equal to {result:.1F} mb")

    elif d_choose == 5:
        def gb_to_tb(gb):
            return gb/1000
        gb=float(input("enter data value in gb:"))
        result=gb_to_tb(gb)
        print(f"{gb} gb is equal to {result:.1F} tb")

    elif d_choose == 6:
        def tb_to_gb(tb):
            return tb*1000
        tb=float(input("enter data value in tb:"))
        result=tb_to_gb(tb)
        print(f"{tb} tb is equal to {result:.1F} gb")

    else:
        print("something went wrong in data function")

#------------------------ end -------------------------#



#---------------- temperature function ----------------#

elif type_choose == 5:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in t:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    t_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if t_choose == 1:
        def celcius_to_farenheit(celcius):
            return (celcius*9/5) + 32
        celcius=float(input("enter temperature in celcius:"))
        result=celcius_to_farenheit(celcius)
        print(f"{celcius} celcius is equal to {result:.1F} farenheit")

    elif t_choose == 2:
        def farenheit_to_calcius(farenheit):
            return (farenheit-32)*5/9
        farenheit=float(input("enter temperature in farenheit:"))
        result=farenheit_to_calcius(farenheit)
        print(f"{farenheit} farenheit is equal to {result:.1F} celcius")

    elif t_choose == 3:
        def celcius_to_kelvin(celcius):
            return celcius+273.15
        celcius=float(input("enter temperature in celcius:"))
        result=celcius_to_kelvin(celcius)
        print(f"{celcius} celcius is equal to {result:.1F} kelvin")

    elif t_choose == 4:
        def kelvin_to_celcius(kelvin):
             return kelvin-273.15
             kelvin=float(input("enter temperature in kelvin:"))
             result=kelvin_to_celcius(kelvin)
             print(f"{kelvin} kelvin is equal to {result:.1F} celcius ")
    else:
         print("something went wrong in temperature function")

#------------------------ end -------------------------#



#-------------------- time function -------------------#

elif type_choose == 6:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in T:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    T_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if T_choose == 1:
        def seconds_to_minutes(seconds):
            return seconds/60
        seconds=float(input("enter time in seconds:"))
        result=seconds_to_minutes(seconds)
        print(f"{seconds} seconds is equal to {result:.1F} minutes")

    elif T_choose == 2:
        def minutes_to_seconds(minutes):
            return minutes*60
        minutes=float(input("enter time in minutes:"))
        result=minutes_to_seconds(minutes)
        print(f"{minutes} minutes is equal to {result:.1F} seconds")

    elif T_choose == 3:
        def minutes_to_hours(minutes):
            return minutes/60
        minutes=float(input("enter time in minutes:"))
        result=minutes_to_hours(minutes)
        print(f"{minutes} minutes is equal to {result:.1F} hours")

    elif T_choose == 4:
        def hours_to_minutes(hours):
            return hours*60
        hours=float(input("enter time in hours:"))
        result=hours_to_minutes(hours)
        print(f"{hours} hours is equal to {result:.1F} minutes")

    elif T_choose == 5:
        def hours_to_days(hours):
            return hours/24
        hours=float(input("enter time in hours:"))
        result=hours_to_days(hours)
        print(f"{hours} hours is equal to {result:.1F} days")

    elif T_choose == 6:
        def days_to_hours(days):
            return days*24
        days=float(input("enter days:"))
        result=days_to_hours(days)
        print(f"{days} days is equal to {result:.1F} days")

    else:
        print("something went wrong in time function")

#------------------------ end -------------------------#



#-------------------- days function -------------------#

elif type_choose == 7:
    subprocess.run(["clear"])
    count=0
    print("\n")
    for items in D:
        count+=1
        print(Style.BRIGHT+Fore.GREEN+f"{count} {items}{"\n"}")
    D_choose=int(input(Style.BRIGHT+Fore.YELLOW+"choose an option:"))

    if D_choose==1:
        def days_to_weeks(days):
            return days/7
        days=int(input("enter days:"))
        result=days_to_weeks(days)
        print(f"{days} days are equal to {result:.1F} weeks")

    elif D_choose==2:
        def weeks_to_days(weeks):
            return weeks*7
        weeks=int(input("enter weeks:"))
        result=weeks_to_days(weeks)
        print(f"{weeks} weeks are equal to {result:.1F} days")

    elif D_choose==3:
        def days_to_months(days):
            return days/30.44
        days=int(input("enter days:"))
        result=days_to_months(days)
        print(f"{days} days are equal to {result:.1F} months")

    elif D_choose==4:
        def months_to_days(months):
            return months*30.44
        months=int(input("enter months:"))
        result=months_to_days(months)
        print(f"{months} months are equal to {result:.1F} days")

    elif D_choose==5:
        def days_to_years(days):
            return days/365
        days=int(input("enter days:"))
        result=days_to_years(days)
        print(f"{days} days are equal to {result:.1F} years")

    elif D_choose==6:
        def years_to_days(years):
            return years*365
        years=int(input("enter years:"))
        result=years_to_days(years)
        print(f"{years} years are equal to {result:.1F} days")

    else:
        print("something went wrong in days function")

#------------------------ end -------------------------#




