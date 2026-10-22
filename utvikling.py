"""print("Hei")

navn = input("Hva er navnet ditt ? ")
alder = int(input("Hvor gammel er du ? "))
farge = input("Hva er ditt favorittfarge? ")

print(f"Hei, {navn} du er {alder} og du liker {farge}")



rett1 = input("Skriv inn favorittrett 1 ")
rett2 = input("Skriv inn favorittrett 2 ")
rett3 = input("Skriv inn favorittrett 3 ")

favoritter = [ rett1, rett2, rett3 ]

print(f"dine favoritter er {favoritter}")



navn = input("Hva er navnet ditt? ")
alder = int(input("Hvor gammel er du? "))
by = input("Hvor bor du ? ")
hobby = input("Hva er din hobby? ")

print("===== PROFIL =====")
print(f"Navn:   {navn}")
print(f"Alder: {alder}")
print(f"Bor i: {by}")
print(f"Hobby:  {hobby}")
print("===================")

ord = "PROGRAMMERING"   
print (ord[0])
print (ord[3:8])
print (ord[::-1])

    
alder = int(input("Hvor gammel er du? "))
if alder >= 18:
    print("Du er gammle nok til å stemme!")
else:


print("Her kan du sjekke om du kan kjøre bil!")

alder = int(input("Hvor gammel er du? "))
har_lappen = True

if alder >= 18 and har_lappen:
    print("DU KAN KJØRE BIL!")
else:
    print("Du kan ikke kjøre bil !")

er_regn = False
if not er_regn:
    print("Vi kan gå ut")
else: 
    print("Vi kan ikke gå ut :( ")

"""

def presenter(navn, alder):
    print(f"Jeg heter {navn} og er {alder} år gammel! ")

presenter ("Kari", 23)