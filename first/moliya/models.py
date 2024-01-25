from django.db import models

# Create your models here.

TURLAR = [
    ("HP", "HP"),
    ("Acer", "Acer"),
    ("Asus", "Asus"),
    ("Lenovo", "Lenovo"),
]

class Notebook(models.Model):
    nom = models.CharField(max_length=30, choices=TURLAR)
    model = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    yangi = models.BooleanField(default=False)
    rasm = models.FileField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nom}  {self.model}"



class Imtihon(models.Model):
    nom = models.CharField(max_length=30)
    sana = models.DateField()
    talaba_soni = models.BigIntegerField()
    sayt = models.CharField(max_length=30)
    yillik = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nom}  {self.sana}  {self.talaba_soni}"

Jinslar = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol"),
]

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    yosh = models.BigIntegerField()
    jins = models.CharField(max_length=30,choices=Jinslar)
    def __str__(self):
        return f"{self.ism}  {self.email}  {self.jins}"


class Foydalanuvchi(models.Model):
    username = models.CharField(max_length=30, unique=True)
    login = models.CharField(max_length=30, unique=True)
    parol = models.BigIntegerField()
    email = models.CharField(max_length=30,choices=Jinslar)
    talaba = models.CharField(max_length=30, choices=Jinslar)
    rasm = models.FileField()
    def __str__(self):
        return f"{self.ism}  {self.email}  {self.jins}"


class Profil(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    yosh = models.BigIntegerField()
    jins = models.CharField(max_length=30,choices=Jinslar)
    def __str__(self):
        return f"Ism:{self.ism}  Tel:{self.tel} Yosh: {self.yosh}"
darajalar = [
    ("Boshlang'ich", "Boshlang'ich"),
    ("O'rta", "O'rta"),
    ("Yuqori", "Yuqori"),
]
class Kurs(models.Model):
    nom = models.CharField(max_length=30)
    daraja = models.CharField(max_length=30,choices=darajalar)
    narx = models.BigIntegerField()
    chegirma = models.CharField(max_length=30,default=0)
    def __str__(self):
        return f"Nom:{self.nom}  Narx:{self.narx} Chegirma: {self.chegirma}"

xolat = [
    ("Tugatildi", "Tugatildi"),
    ("Davom etyabdi", "Davom etyapti"),
    ("Boshlanmagan", "Boshlanmagan"),
]
class Xarid(models.Model):
    profile=models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs=models.ForeignKey(Kurs, on_delete=models.CASCADE)
    sana=models.DateField()
    holat=models.CharField(max_length=20,choices= xolat)
    def __str__(self):
        return f"Sana:{self.sana}"

class Izoh(models.Model):
    baho=models.CharField(max_length=20)
    matn=models.CharField(max_length=20)
    sana=models.DateField()
    profil=models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    def __str__(self):
        return f"Sana:{self.sana}"

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.profil}     {self.kurs}"



