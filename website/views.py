import os

from django.shortcuts import render, redirect
from django.utils import timezone
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, pdf
import io

from reportlab.platypus import SimpleDocTemplate

from .forms import KidsEnroll, CampEnroll


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
    return render(request, 'website/przedszkola.html', {'form': form})


def thanks(request):
    return render(request, 'website/thanks.html')


def kids_enroll_camp(request):
    file_path = "website/templates/static/oboz.pdf"
    doc = SimpleDocTemplate(file_path)
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
            output_filename = '/home/{}/Desktop/umowa.pdf'.format(username, output).encode('UTF-8', errors='ignore').decode('UTF-8', errors='igoner')
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




    else:
        form = CampEnroll()
    return render(request, 'website/oboz_zapis.html', {'form': form})
