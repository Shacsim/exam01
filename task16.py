narx = 100000
yosh = int(input("Yoshingizni kiriting: "))

chegirma = 0

if 0 <= yosh <= 6:
    chegirma = 50
elif 7 <= yosh <= 17:
    chegirma = 20
elif yosh >= 60:
    chegirma = 30

chegirma_summasi = narx * chegirma / 100
yakuniy_narx = narx - chegirma_summasi

print(f"Chegirma: {chegirma}%")
print(f"Chegirma summasi: {int(chegirma_summasi)} so'm")
print(f"To'lanadigan narx: {int(yakuniy_narx)} so'm")