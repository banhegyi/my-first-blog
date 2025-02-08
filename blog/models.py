from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

# class Post(models.Model): ez a sor definiálja a modellünket (ami egy objektum)

'''
a class egy speciális kulcsszó, ami azt mutatja meg, hogy éppen egy objektumot definiálunk.
a Post a modellünk neve. Más nevet is adhatnál neki (de kerüld el a speciális karaktereket
- pl ékezetes karakterek - és a szóközt). Az osztályok (classok) nevét mindig nagybetűvel kezdjük.
a models.Model azt jelenti, hogy a Post egy Django Model, így a Django tudni fogja, hogy el kell menteni az adatbázisba.
Most pedig azokat a tulajdonságokat definiáljuk, amikről korábban beszéltünk:title (cím), text (szöveg),
created_date (létrehozás dátuma), published_date (közzététel dátuma) és author (szerző). 
Ahhoz, hogy ezt megtehessük, mindegyik mezőnek meg kell határoznunk a típusát (Szöveg lesz benne?
Egy szám? Dátum? Egy másik objektumhoz fog kapcsolni, például egy User-hez (felhasználó)?).

models.CharField - így definiálsz olyan szövegmezőt, ami meghatározott számú karaktert tartalmazhat.
models.TextField - ez hosszú szövegekhez van, korlátozás nélkül. Pont jó egy blogbejegyzéshez, igaz?
models.DateTimeField - ez dátumot és időt tartalmaz.
models.ForeignKey - ez egy másik modellel való kapcsolatot jelent.
'''

class Post(models.Model):    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
És mi a helyzet a def publish(self): résszel? Ez pontosan az a publish (közzététel) method, amiről korábban beszéltünk.
A def azt jelenti, hogy ez egy függvény (function) / method, és a publish ennek a methodnak a neve. Ha szeretnéd, 
megváltoztathatod a metódus nevét. Az a szabály, hogy csak kisbetűket használunk, és szóköz helyett underscore-t (alulvonás).
Például egy olyan method neve, ami az átlagárat számolja ki, ez lehetne: calculate_average_price.

A methodok gyakran return-ölnek (visszaadnak) valamit. Erre van is egy példa a __str__ methodban. Ebben az esetben amikor
meghívjuk a __str__()-t, egy szöveget kapunk vissza (string), ami a Post címe.

Vedd észre azt is, hogy mind def publish(self): mind def __str__(self): indentálva van a class-on bellül. Python számára
fontosak a szóközök, ezért a method-okat indentálni kell az osztályokon bellül. Ha ez elmarad, akkor a method nem az adott
osztályhoz fog tartozni, és furcsán fog viselkedni a program.
'''