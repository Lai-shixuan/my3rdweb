from django.http import JsonResponse
import cv2
import base64
from PIL import Image
import numpy as np
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # 为简化起见，暂时禁用CSRF。实际部署时应考虑安全性。
def process_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        file_bytes = image.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        processed_image = img
        processed_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        processed_image2 = processed_image.crop((50, 50, 100, 100))


        buffer = BytesIO()
        processed_image2.save(buffer, format="JPEG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        # print(image_base64)

        return JsonResponse({'image': image_base64})
