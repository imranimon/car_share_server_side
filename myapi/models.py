from django.db import models


class Benutzer(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'benutzer'

    def __str__(self):
        return self.name


class Fahrerlaubnis(models.Model):
    nummer = models.SmallAutoField(primary_key=True)
    benutzer = models.ForeignKey(Benutzer, models.DO_NOTHING)
    ablaufdatum = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fahrerlaubnis'

    def __str__(self):
        return self.nummer


class Transportmittel(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    icon = models.TextField()

    class Meta:
        managed = False
        db_table = 'transportmittel'

    def __str__(self):
        return self.name


class Fahrt(models.Model):
    id = models.SmallAutoField(primary_key=True)
    startort = models.CharField(max_length=100)
    zielort = models.CharField(max_length=100)
    fahrtdatumzeit = models.DateTimeField()
    maxplaetze = models.SmallIntegerField()
    fahrtkosten = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=11)
    benutzer = models.ForeignKey(Benutzer, models.DO_NOTHING)
    transportmittel = models.ForeignKey('Transportmittel', models.DO_NOTHING)
    beschreibung = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fahrt'

    def __str__(self):
        return self.startort


class Reservieren(models.Model):
    id = models.SmallAutoField(primary_key=True)
    benutzer = models.ForeignKey(Benutzer, models.DO_NOTHING)
    fahrt = models.ForeignKey(Fahrt, models.DO_NOTHING)
    anzplaetze = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'reservieren'
        unique_together = (('fahrt', 'benutzer'),)

    def __str__(self):
        return self.id


class Bewertung(models.Model):
    id = models.SmallAutoField(primary_key=True)
    benutzer = models.ForeignKey(Benutzer, models.DO_NOTHING)
    fahrt = models.ForeignKey(Fahrt, models.DO_NOTHING)
    textnachricht = models.CharField(max_length=2000)
    erstellungsdatum = models.DateTimeField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bewertung'
        unique_together = (('benutzer', 'fahrt'),)

    def __str__(self):
        return self.id
