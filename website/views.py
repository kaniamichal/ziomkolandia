import io
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from newsletter.forms import JoinForm
from ziomkolandia import settings
from .forms import KidsEnroll, CampEnroll, DayCampEnroll, ContactForm


# def index(request):
#      return render(request, 'website/index.html')

def index(request):
    return render(request, 'website/index.html')


def kids_enroll(request):
    if request.method == "POST":
        form = KidsEnroll(request.POST)
        if form.is_valid():
            kindergarten = form.save(commit=False)
            kindergarten.data_enrol = timezone.now()
            #  kindergarten.regulations(required=True)
            kindergarten.save()
            return redirect('thanks')
    else:
        form = KidsEnroll()
    return render(request, 'website/przedszkola-zapisy.html', {'form': form})


def kids_enroll_camp(request):
    file_path = "website/templates/static/oboz.pdf"
    if request.method == "POST":
        form = CampEnroll(request.POST)
        if form.is_valid():
            camp = form.save(commit=False)
            camp.data_enrol = timezone.now()
            parent_name = form.cleaned_data['parent_name']
            parent_email = form.cleaned_data['parent_email']
            child_name = form.cleaned_data['child_name']
            child_birth_date = form.cleaned_data['child_birth_date']
            child_born_city = form.cleaned_data['child_born_city']
            child_pesel = form.cleaned_data['child_pesel']
            street_address = form.cleaned_data['street_address']
            postal_code = form.cleaned_data['postal_code']
            city_address = form.cleaned_data['city_address']
            phone_parent_1 = form.cleaned_data['phone_parent_1']
            phone_parent_2 = form.cleaned_data['phone_parent_2']
            school_name = form.cleaned_data['school_name']
            school_address = form.cleaned_data['school_address']
            school_class = form.cleaned_data['school_class']
            interests_child = form.cleaned_data['interests_child']
            print(child_name, child_birth_date, interests_child)
            # camp.save()
            # creating a contract file to camp as pdf file

            pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=A4)
            c.setFont('DejaVuSans', 10, True)
            c.drawString(200, 453, child_name)
            c.drawString(155, 412, child_birth_date)
            c.drawString(290, 412, child_pesel)
            c.drawString(180, 370, street_address)
            c.drawString(250, 330, postal_code)
            c.drawString(320, 330, city_address)
            c.drawString(190, 303, school_name)
            c.drawString(190, 288, school_address)
            c.drawString(110, 246, school_class)
            c.drawString(205, 205, interests_child)
            c.showPage()
            c.save()

            buffer2 = io.BytesIO()
            d = canvas.Canvas(buffer2, pagesize=A4)
            d.setFont('DejaVuSans', 10, True)
            d.drawString(305, 591, parent_name)
            d.drawString(125, 566, phone_parent_1)
            d.drawString(325, 566, parent_email)
            d.drawString(214, 544, child_name)
            d.drawString(216, 520, child_birth_date)
            d.drawString(432, 520, child_born_city)
            d.drawString(178, 498, street_address)
            d.drawString(430, 498, postal_code)
            d.drawString(490, 498, city_address)
            d.showPage()
            d.save()

            buffer3 = io.BytesIO()
            e = canvas.Canvas(buffer3, pagesize=A4)
            e.setFont('DejaVuSans', 10, True)
            e.drawString(225, 782, child_name)
            e.showPage()
            e.save()

            buffer.seek(0)
            buffer2.seek(3)
            buffer3.seek(8)

            changes = PdfFileReader(buffer)
            changes2 = PdfFileReader(buffer2)
            changes3 = PdfFileReader(buffer3)
            original = PdfFileReader(open(file_path, "rb"))
            reader = PdfFileReader(file_path)
            output: PdfFileWriter = PdfFileWriter()
            page = original.getPage(0)
            page.mergePage(changes.getPage(0))
            output.addPage(page)
            output.addPage(reader.getPage(1))
            output.addPage(reader.getPage(2))
            page2 = original.getPage(3)
            page2.mergePage(changes2.getPage(0))
            output.addPage(page2)
            output.addPage(reader.getPage(4))
            output.addPage(reader.getPage(5))
            output.addPage(reader.getPage(6))
            output.addPage(reader.getPage(7))
            page3 = original.getPage(8)
            page3.mergePage(changes3.getPage(0))
            output.addPage(page3)

            # with open("output.pdf", "wb") as output_stream:
            # myFile = File(output_stream)
            username = os.getenv('USER')
            output_filename = '/home/{}/Desktop/umowa.pdf'.format(username, output).encode('UTF-8',
                                                                                           errors='ignore').decode(
                'UTF-8', errors='igoner')
            with open(output_filename, "wb+") as out:
                output.write(out)

            # output_stream = open("output.pdf", "wb+")
            # output.write(output_stream)

            # response = HttpResponse(output, content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="umowa.pdf'
            # output_stream.close()
            camp.save()
            # return response
            # myFile.close()
            # fs = FileSystemStorage()
            # with fs.open(myFile) as pdf:

            # response = HttpResponse(output.addAttachment("output2.pdf", output_stream), content_type='application/pdf')

            # response = HttpResponse((output_stream.getvalue()), content_type='application/pdf')
            # response = HttpResponse((output_stream.getvalue()), content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename=umowa.pdf'
            # # response.write(output.getValue())
            # return response
            # end
            # return FileResponse(output, as_attachment=True, filename="umowa.pdf")
            return redirect('thanks')
            # TODO change all logic with save file and redirect to another page

    else:
        form = CampEnroll()
    return render(request, 'website/oboz-zapisy.html', {'form': form})


def kids_enroll_day_camp(request):
    file_path = "website/templates/static/polkolonie.pdf"
    if request.method == "POST":
        form = DayCampEnroll(request.POST)
        if form.is_valid():
            day_camp = form.save(commit=False)
            day_camp.data_enrol = timezone.now()
            child_name = form.cleaned_data['child_name']
            child_pesel = form.cleaned_data['child_pesel']
            child_birth_date = form.cleaned_data['child_birth_date']
            parent_name = form.cleaned_data['parent_name']
            street_address = form.cleaned_data['street_address']
            postal_code = form.cleaned_data['postal_code']
            city_address = form.cleaned_data['city_address']
            parent_email = form.cleaned_data['parent_email']
            phone_parent_1 = form.cleaned_data['phone_parent_1']
            phone_parent_2 = form.cleaned_data['phone_parent_2']
            receiving_person_1 = form.cleaned_data['receiving_person_1']
            relationship_child_1 = form.cleaned_data['relationship_child_1']
            phone_receiving_1 = form.cleaned_data['phone_receiving_1']
            receiving_person_2 = form.cleaned_data['receiving_person_2']
            relationship_child_2 = form.cleaned_data['relationship_child_2']
            phone_receiving_2 = form.cleaned_data['phone_receiving_2']
            receiving_person_3 = form.cleaned_data['receiving_person_3']
            relationship_child_3 = form.cleaned_data['relationship_child_3']
            phone_receiving_3 = form.cleaned_data['phone_receiving_3']

            # camp.save()
            # creating a contract file to camp as pdf file

            pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
            buffer = io.BytesIO()
            c = canvas.Canvas(buffer, pagesize=A4)
            c.setFont('DejaVuSans', 10, True)
            c.drawString(130, 580, child_name)
            c.drawString(120, 553, child_pesel)
            c.drawString(130, 524, child_birth_date)
            c.drawString(130, 442, parent_name)
            c.drawString(130, 387, street_address)
            c.drawString(130, 359, postal_code)
            c.drawString(230, 359, city_address)
            c.drawString(130, 332, parent_email)
            c.drawString(130, 303, phone_parent_1)
            c.drawString(190, 276, phone_parent_2)
            c.drawString(60, 159, receiving_person_1)
            c.drawString(260, 159, relationship_child_1)
            c.drawString(440, 159, phone_receiving_1)
            c.drawString(60, 127, receiving_person_2)
            c.drawString(260, 127, relationship_child_2)
            c.drawString(440, 127, phone_receiving_2)
            c.drawString(60, 95, receiving_person_3)
            c.drawString(260, 95, relationship_child_3)
            c.drawString(440, 95, phone_receiving_3)
            c.setFont('DejaVuSans', 10, True)
            c.showPage()
            c.save()

            buffer.seek(0)
            changes_day_camp = PdfFileReader(buffer)
            original = PdfFileReader(open(file_path, "rb"))
            reader = PdfFileReader(file_path)
            output: PdfFileWriter = PdfFileWriter()
            page = original.getPage(0)
            page.mergePage(changes_day_camp.getPage(0))
            output.addPage(page)
            output.addPage(reader.getPage(1))
            output.addPage(reader.getPage(2))
            output.addPage(reader.getPage(3))

            # with open("output.pdf", "wb") as output_stream:
            # myFile = File(output_stream)
            ### savve file to desktop
            # username = os.getenv('USER')
            # output_filename = '/home/{}/Desktop/umowa-polkolonie.pdf'.format(username, output).encode('UTF-8',
            #                                                                                           errors='ignore').\
            #     decode('UTF-8', errors='ignore')
            # with open(output_filename, "wb+") as out:
            #     output.write(out)

            # output_stream = open("output.pdf", "wb+")
            # output.write(output_stream)

            # response = HttpResponse(output, content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="umowa.pdf'
            # output_stream.close()
            # return response
            # myFile.close()
            # fs = FileSystemStorage()
            # with fs.open(myFile) as pdf:

            # response = HttpResponse((output_stream.getvalue()), content_type='application/pdf')
            # response = HttpResponse(out, content_type='application/pdf')
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=umowa-polkolonie.pdf'
            output.write(response)
            # response.write(out)
            # return response
            day_camp.save()
            form = DayCampEnroll()

            # # response.write(output.getValue())
            return response, redirect('thanks')

            # end
            # return FileResponse(output, as_attachment=True) #filename="umowa2.pdf")
            # return redirect('thanks')
            # return redirect('thanks')

    else:
        form = DayCampEnroll()
    return render(request, 'website/polkolonie-zapisy.html', {'form': form})
# TODO change all logic with save file and redirect to another page


def contact_form(request):
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        name = request.POST.get('contact_name', '')
        subject = request.POST.get('contact_title', '')
        email = request.POST.get('contact_email', '')
        message = request.POST.get('content', '')
        if form.is_valid() and email and name:
            print(name, message)
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['info@ziomkolandia.pl'], fail_silently=False)
            # return redirect('contact')
            # except BadHeaderError:
            #     return HttpResponse('Something has wrong')
            messages.success(request, "Wiadomość została wysłana")
            return redirect('contact')

    return render(request, 'website/contact.html', {
        'form': form,
    })


# newsletter
# TODO move to newsletter apps



def thanks(request):
    return render(request, 'website/thanks.html')


def contact(request):
    return render(request, 'website/contact.html')


def przedszkola(request):
    return render(request, 'website/przedszkola.html')


def camps(request):
    return render(request, 'website/obozy.html')


def offer(request):
    return render(request, 'website/oferta.html')


def atractions(request):
    return render(request, 'website/atrakcje.html')


def eventy(request):
    return render(request, 'website/eventy.html')


def green(request):
    return render(request, 'website/zielona-szkola.html')


def crash_kader(request):
    return render(request, 'website/atrakcje/CrashKader.html')


def crash_runner(request):
    return render(request, 'website/atrakcje/CrashRunner.html')


def klocki_maxi(request):
    return render(request, 'website/atrakcje/KoloroweKlockiMaxi.html')


def archery_tag(request):
    return render(request, 'website/atrakcje/ArcheryTag.html')


def bumper_ball(request):
    return render(request, 'website/atrakcje/BumperBall.html')


def zjazd_klocki(request):
    return render(request, 'website/atrakcje/ZjezdzalniaKlocki.html')


def climbing_wall(request):
    return render(request, 'website/atrakcje/ClimbingWall.html')


def dmuchaniec_klocki(request):
    return render(request, 'website/atrakcje/DmuchaniecKlocki.html')


def skakaniec_klocki(request):
    return render(request, 'website/atrakcje/SkakaniecKlocki.html')


def poducha_wodna(request):
    return render(request, 'website/atrakcje/PoduchaWodna.html')


def motorowka(request):
    return render(request, 'website/atrakcje/Motorowka.html')


def offer_green(request):
    return render(request, 'website/oferta-zielona-szkola.html')


def green_mini(request):
    return render(request, 'website/zielona-szkola/ziomkolandia-mini.html')


def green_maxi(request):
    return render(request, 'website/zielona-szkola/ziomkolandia-maxi.html')


def green_xl(request):
    return render(request, 'website/zielona-szkola/ziomkolandia-xl.html')