from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nama Studio")
    address = models.TextField(verbose_name="Alamat")
    phone_number = models.CharField(max_length=20, verbose_name="Nomor Telepon")

    def __str__(self):
        return self.name

class Photographer(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, verbose_name="Studio")
    name = models.CharField(max_length=255, verbose_name="Nama Fotografer")

    def __str__(self):
        return self.name

class Photoshoot(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE, verbose_name="Fotografer")
    date = models.DateField(verbose_name="Tanggal")
    duration = models.DurationField(verbose_name="Durasi")
    location = models.CharField(max_length=255, verbose_name="Lokasi")

    def __str__(self):
        return f"{self.photographer.name} - {self.date}"
