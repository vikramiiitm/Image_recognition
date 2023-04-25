import os

from PIL.ImagePath import Path
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from image_recognition.settings import BASE_DIR
from .models import Image
from .serializers import ImageSerializer
from rest_framework.viewsets import ModelViewSet
import pandas as pd
from django.core.files import File



# Create your views here.


class ImageViewset(ModelViewSet):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
    queryset = Image.objects.all()

    def create(self, request):
        data = request.data
        file_csv = request.FILES.get('data_csv')
        df = pd.read_csv(file_csv)
        print(df.columns)
        for i,j in df.iterrows():
            data = {}
            data['title'] = j['image_name']
            data['objects_detected'] = j['objects_detected']
            data['timestamp'] = j['timestamp']
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            img_obj = serializer.save()
            image_path = os.path.join(BASE_DIR, 'recognize', 'static', 'images', j['image_name'])

            # open the image and save it image fields
            local_file = open(image_path, "rb")
            djangofile = File(local_file)
            img_obj.image.save(f'{j["image_name"]}', djangofile)
            local_file.close()

            img_obj.save()
        return Response({'data':data})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        from_ = request.GET.get('from')
        to_ = request.GET.get('to')
        if from_ and to_:
            img = queryset.filter(timestamp__gte=from_, timestamp__lte=to_)
            serializer = self.serializer_class(img, many=True)
            return Response({"data": serializer.data})
        else:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"data": serializer.data})