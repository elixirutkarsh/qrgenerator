from django.shortcuts import render
import qrcode

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill='black', back_color='white')
        response = HttpResponse(content_type="image/png")
        image.save(response, "PNG")
        return response
    else:
        return render(request, 'generate_qr.html')
