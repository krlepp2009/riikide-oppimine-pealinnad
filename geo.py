from random import shuffle

d='''aas: Küpros - Nikosia; Türgi - Ankara; Kasahstan - Astana; Hiina Rahvavabariik - Peking; Lõuna-Korea - Soul; Jaapani Keisririik - Tokyo; Filipiinid - Manila; Indoneesia - Jakarta; Malaisia - Kuala-Lumpur; Vietnam - Hanoi; Tai Kuningriik - Bangkok; Bangladesh - Dhaca; India - New Delhi; Sri-Lanka - Colombo; Pakistan - Islamabad; Afganistan - Kabul; Iraan - Teheran; Iraak - Bagdad; Süüria - Damaskus; Iisrael - Jeruusalemm; Liibanon - Beirut; Jordaania Hašimiidi Kuningriik - Amman; Araabia Ühendemiraadid - Abu Dhabi; Saudi-Araabia Kuningrik - Ar-Riyad; Gruusia (Georgia) - Thbilisi; Armeenia - Jerevan; Aserbaidžaan - Bakuu
aust: Austraalia - Canberra; Uus Meremaa - Wellington
aaf: Maroko Kuningriik - Rabat; Alžeeria - Alžiir; Tuneesia - Tunis; Liibüa - Tripoli; Egiptuse Araabia Vabariik (Egiptus) - Kairo; Sudaan - Hartum; Etioopia - Addis-Abeba; Senegal - Dakar; Kongo Demokraatlik Vabariik - Kinshasa; Angola - Luanda; Namiibia - Windhoek; Lõuna-Aafrika Vabariik - Pretoria; Kenya - Nairobi; Sambia - Lusaka; Madagaskar - Antananarivo
pam: Kanada - Ottawa; Ameerika Ühendriigid - Washington; Mehhiko - Mexico; Kuuba - Havanna
lam: Venezuela - Caracas; Peruu - Lima; Tšiili - Santiago; Argentiina - Buenos Aires; Uruguay - Montevideo; Brasiilia - Brasilia; Kolumbia - Bogota'''.splitlines()
d=[s.split(": ") for s in d]
d={s[0]:s[1].split("; ") for s in d}
li=input("sisesta ala(d) (aas, aust, aaf, pam, lam) eraldamiseks kasuta tühikut: ").split()
actd=[]
for a in li:
    actd.extend(d[a])
actd=[[s.split(" - ")[0],s.split(" - ")[1],-1] for s in actd]
shuffle(actd)

i=0
while i<len(actd):
    a=actd[i]
    p=input(f"{a[0]} - ").strip().lower()
    if p!=a[1].lower():
        p=input(f"vihje: {a[0]} - {a[1][0]}{'-'*(len(a[1])-1)} - ").strip().lower()
        if p!=a[1].lower():
            while p!=a[1].lower():
                p=input(f"vale! {a[0]} - {a[1]} - ").strip().lower()
            if a[2]==-1:
                a[2]=3
            if i!=len(actd)-1:
                actd.insert(i+3,a)
        else:
            '''if a[2]==-1 or a[2]==1:
                i+=1
                print("\n"*30)
                continue
            a[2]-=1'''
            if a[2]==-1:
                a[2]=3
            if i!=len(actd)-1:
                actd.insert(i+3,a)
    else:
        if a[2]==-1 or a[2]==1:
            i+=1
            print("\n"*30)
            continue
        a[2]-=1
        if i!=len(actd)-1:
            actd.insert(i+3,a)
    print("\n"*30)
    i+=1