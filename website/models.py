from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django import forms


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
    JACEKAGATKA = 'Przedszkole im. Jacka i Agatki w Człuchowie'
    BAJKA = 'Przedszkole Bajka w Człuchowie'
    SMYK = 'Przedszkole Smyk w Człuchowie'
    PIANO = 'Przedszkole Piano w Człuchowie'
    KINDER_NAME_CHOICES = [
        (DEBRZNO, "Przedszkole w Debrznie"),
        (WIERZCHOWO, 'Przedszkole w Wierzchowie Człuwoskim'),
        (JACEKAGATKA, 'Przedszkole im. Jacka i Agatki w Człuchowie'),
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

    user_name = models.CharField(max_length=200, verbose_name="Imię i nazwisko rodzica (opiekuna)")
    child_name = models.CharField(max_length=200, verbose_name="Imię i nazwisko dziecka")
    class_name = models.CharField(max_length=50, verbose_name="Nazwa grupy przedszkolnej")
    phone_number = models.CharField(max_length=9,
                                    verbose_name='Nr telefonu rodzica (opiekuna)',
                                    validators=[PHONE_NUMBER_REGEX])
    email = models.EmailField(max_length=254, null=True, verbose_name='Adres mailowy rodzica (opiekuna)')
    regulations = models.BooleanField(verbose_name='Potwierdzam, że zapoznałem się z regulaminem',
                                      validators=[validate_regulations])
    data_enrol = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kinder_name + ' | ' + self.user_name + ' | ' + str(self.data_enrol)


# Model to the enrolling to the camps
class Camp(models.Model):
    ONLY_NUMBER_REGEX = RegexValidator(r'^[-\s\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')

    parent_name = models.CharField(max_length=255, verbose_name="Imię i nazwisko rodzica/opiekuna")
    parent_email = models.EmailField(verbose_name="Adres mailowy rodzica/opiekuna")
    child_name = models.CharField(max_length=255, verbose_name="Imię i nazwisko dziecka")
    child_birth_date = models.CharField(max_length=10, verbose_name="Data urodzenia (RRRR-MM-DD)")
    child_born_city = models.CharField(max_length=100, null=True, verbose_name="Miejsce urodzenia dziecka")
    child_pesel = models.CharField(max_length=11,
                                   verbose_name="PESEL",
                                   validators=[ONLY_NUMBER_REGEX])
    street_address = models.CharField(max_length=254, verbose_name="Adres zamieszkania (ulica, nr domu, nr mieszkania)")
    postal_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city_address = models.CharField(max_length=100, verbose_name="Miejscowość")
    phone_parent_1 = models.CharField(max_length=9,
                                      verbose_name="Telefon kontaktowy nr 1 do rodzica/opiekuna",
                                      validators=[ONLY_NUMBER_REGEX])
    phone_parent_2 = models.CharField(max_length=9,
                                      verbose_name="Telefon kontaktowy nr 2 do rodzica/opiekuna",
                                      validators=[ONLY_NUMBER_REGEX])
    school_name = models.CharField(max_length=255, verbose_name="Nazwa Szkoły")
    school_address = models.CharField(max_length=255, verbose_name="Adres szkoły (ulica, kod pocztowy, miejscowość")
    school_class = models.CharField(max_length=2, verbose_name="Klasa do której dziecko uczęszcza")
    interests_child = models.CharField(max_length=255,
                                       verbose_name="Zainteresowania dziecka (wymienić kilka najważniejszych "
                                                    "oddzielając przecinkiem) ")
    data_enrol = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.child_name + ' | ' + self.city_address + ' | ' + str(self.data_enrol)


# Model to enroll to the day camps
class DayCamp(models.Model):
    ONLY_NUMBER_REGEX = RegexValidator(r'^[-\s\./0-9]*$', 'Podaj poprawny nr tefonu - tylko liczby')

    FIRST = 'I termin'
    SECOND = 'II termin'

    DATE_CHOICE = [
        (FIRST, 'I termin'),
        (SECOND, 'II termin'),
    ]
    date_daycamp = models.CharField(max_length=9,
                                    choices=DATE_CHOICE,
                                    default=FIRST,
                                    verbose_name='Wybierz termin półkolonii')
    child_name = models.CharField(max_length=255, verbose_name="Imię i nazwisko dziecka")
    child_pesel = models.CharField(max_length=11,
                                   verbose_name="PESEL dziecka",
                                   validators=[ONLY_NUMBER_REGEX])
    child_birth_date = models.CharField(max_length=10, verbose_name="Data urodzenia dziecka (RRRR-MM-DD)")
    parent_name = models.CharField(max_length=255, verbose_name="Imię i nazwisko rodzica/opiekuna")
    street_address = models.CharField(max_length=254, verbose_name="Adres zamieszkania (ulica, nr domu, nr mieszkania)")
    postal_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city_address = models.CharField(max_length=100, verbose_name="Miejscowość")
    parent_email = models.EmailField(verbose_name="Adres mailowy rodzica/opiekuna")
    phone_parent_1 = models.CharField(max_length=9,
                                      verbose_name="Telefon kontaktowy nr 1 do rodzica/opiekuna",
                                      validators=[ONLY_NUMBER_REGEX])
    phone_parent_2 = models.CharField(max_length=9,
                                      verbose_name="Telefon kontaktowy nr 2 do rodzica/opiekuna",
                                      validators=[ONLY_NUMBER_REGEX])
    receiving_person_1 = models.CharField(max_length=255,
                                          null=True,
                                          verbose_name="Imię i nazwisko osoby upoważnionej do dobioru dziecka")
    relationship_child_1 = models.CharField(max_length=255,
                                            null=True,
                                            verbose_name="Relacje z dzieckiem (dziadek, wujek, "
                                                         "sąsiadka)")
    phone_receiving_1 = models.CharField(max_length=9,
                                         null=True,
                                         verbose_name="Telefon kontaktowy do osoby upoważnionej do odbioru",
                                         validators=[ONLY_NUMBER_REGEX])
    receiving_person_2 = models.CharField(max_length=255,
                                          null=True,
                                          verbose_name="Imię i nazwisko osoby upoważnionej do dobioru dziecka",
                                          default='-----',
                                          help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian")
    relationship_child_2 = models.CharField(max_length=255,
                                            null=True,
                                            verbose_name="Relacje z dzieckiem (dziadek, wujek, sąsiadka)",
                                            default='-----',
                                            help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian")
    phone_receiving_2 = models.CharField(max_length=9,
                                         null=True,
                                         verbose_name="Telefon kontaktowy do osoby upoważnionej do odbioru",
                                         validators=[ONLY_NUMBER_REGEX],
                                         default='-----',
                                         help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian")
    receiving_person_3 = models.CharField(max_length=255,
                                          null=True,
                                          verbose_name="Imię i nazwisko osoby upoważnionej do dobioru dziecka",
                                          default='-----',
                                          help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian")
    relationship_child_3 = models.CharField(max_length=255,
                                            null=True,
                                            verbose_name="Relacje z dzieckiem (dziadek, wujek, sąsiadka)",
                                            default='-----',
                                            help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian")
    phone_receiving_3 = models.CharField(max_length=9,
                                         null=True,
                                         verbose_name="Telefon kontaktowy do osoby upoważnionej do odbioru",
                                         validators=[ONLY_NUMBER_REGEX],
                                         default='-----',
                                         help_text= "Jezeli upoważniasz tylko 1 osobę pozostaw pole bez zmian",)
    data_enrol = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date_daycamp) + ' | ' + self.child_name + ' | ' + self.city_address + ' | ' + str(
            self.data_enrol)
