from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


# model to the enrolling children for classes ziomkolandia in several kindergartens
class Kindergarten(models.Model):
    def validate_regulations(self):
        if not self:
            raise ValidationError('Musisz zapoznać się z regulaminem')

    PHONE_NUMBER_REGEX = RegexValidator(r'^[-\s\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')

    YES = 'YES'
    NO = 'NO'
    DEBRZNO = 'Przedszkole w Debrznie'
    WIERZCHOWO = 'Przedszkole w Wierzchowie Człuwoskim'
    JACEKAGATKA = 'Przedszkole Jacka i Agatki w Człuchpwie'
    BAJKA = 'Przedszkole Bajka w Człuchowie'
    SMYK = 'Przedszkole Smyk w Człuchowie'
    PIANO = 'Przedszkole Piano w Człuchowie'
    KINDER_NAME_CHOICES = [
        (DEBRZNO, "Przedszkole w Debrznie"),
        (WIERZCHOWO, 'Przedszkole w Wierzchowie Człuwoskim'),
        (JACEKAGATKA, 'Przedszkole Jacka i Agatki w Człuchpwie'),
        (BAJKA, 'Przedszkole Bajka w Człuchowie'),
        (SMYK, 'Przedszkole Smyk w Człuchowie'),
        (PIANO, 'Przedszkole Piano w Człuchowie'),
    ]
    REGULATIONS_CHOICE = [
        (YES, 'Tak'),
        (NO, 'Nie'),
    ]

    kinder_name = models.CharField(
        max_length=255,
        choices=KINDER_NAME_CHOICES,
        default=DEBRZNO,
        verbose_name='Wybierz przedszkole'
    )

    user_name = models.CharField(max_length=200, verbose_name="Imię i nazwisko rodzica(opiekuna)")
    child_name = models.CharField(max_length=200, verbose_name="Imię i nazwisko dziecka")
    class_name = models.CharField(max_length=50, verbose_name="Nazwa grupy przedszkolnej")
    phone_number = models.CharField(max_length=9, verbose_name='Nr telefonu rodzica(opiekuna)',
                                    validators=[PHONE_NUMBER_REGEX])
    email = models.EmailField(max_length=254, null=True, verbose_name='Adres mailowy rodzica(opiekuna)')
    regulations = models.BooleanField(verbose_name='Potwierdzam, że zapoznałem się z regulaminem',
                                      validators=[validate_regulations])
    data_enrol = models.DateTimeField(auto_now=True)


# Model to the enrolling to the camps
class Camp(models.Model):
    user_name = models.CharField(max_length=200)
    child_name = models.CharField(max_length=200)
    child_pesel = models.IntegerField
    street_address = models.CharField(max_length=200)
    postal_code = models.IntegerField
    city_address = models.CharField(max_length=100)
    phone_mather = models.IntegerField
    phone_father = models.IntegerField
    school_name = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)
    interests_child = models.CharField(max_length=255)
    information_about_child = models.TextField
    regulations = models.BooleanField
    data_enrol = models.DateTimeField
