from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# from firebase_admin.storage import storage

from photoupload.models import PhotoModel
from .serializers import PhotoSerializer

class PhotoUploadView(APIView):
    
    # queryset = PhotoModel.objects.all()
    # serializer_class = PhotoSerializer
    
    # permission_classes = []
    def post(self, request):
        try:
            image = request.data["image"]
            photo = PhotoModel.objects.create(image = image, url = url)
            photo.url = photo.image.url
            url = request.data.get("url")
            photo.save()
            return Response(
                {'status':'successfully added !'},
                status=status.HTTP_200_OK

            )
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # '{'ajout':'sucess'}',
        except:
            return Response(
                {'ajout':'failed'},
                status=status.HTTP_400_BAD_REQUEST

            )          
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    # status=status.HTTP_200_OK
        


class GetPhoto(generics.RetrieveAPIView):

    queryset = PhotoModel.objects.all()
    serializer_class = PhotoSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        image_url = instance.image.url
        return Response({"image_url": image_url})

# class PhotoUploadView(APIView):
#     serializers = PhotoSerializer
#     def post(self, request, format=None):
#         try:
#             image = request.data['file']
#             filename = image.name
#             bucket = storage.bucket()
#             blob = bucket.blob(filename)
#             blob.upload_from_file(image)
#             url = blob.public_url
#             print('++++++++++++++++++')
#             print(url)

#             photo = PhotoModel.objects.create(image_url=url)
#             photo.save()
#             return Response({'url': url}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             print('======================================')
#             print(e)
           
#             return Response({'error': 'Failed to upload photo'}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import supabase
# import os

# class PhotoUploadView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Get the uploaded photo file from the request
#         photo = request.FILES.get('image', None)

#         if not photo:
#             return Response({'error': 'No file was submitted.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Initialize Supabase client
#         supabase_url = 'https://vdfwefwkqzdjrhcoetjq.supabase.co'
#         supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZkZndlZndrcXpkanJoY29ldGpxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEzNzkzMzIsImV4cCI6MTk5Njk1NTMzMn0.n5WRC_L3kU9yBt_lkDFJWjRcvAQ4GM0lkpHiDPUlYl0'
#         client = supabase.create_client(supabase_url, supabase_key)

#         # Read file contents from memory
#         file_contents = photo.read()

#         # Upload file to Supabase storage
#         bucket_name = 'photos'
#         client = supabase.create_client(supabase_url, supabase_key)
#         storage = client.storage()
#         response = storage.from_file(bucket_name, photo.name, file_contents)

#         # Get the URL of the uploaded file
#         file_name = response['Key']
#         file_url = f'https://{supabase_url}/storage/v1/object/public/{bucket_name}/{file_name}'

#         # Save the file URL to your PostgreSQL database
#         # Replace with your own logic
#         photo_url = file_url
#         photo.save()

#         return Response({'photo_url': photo_url}, status=status.HTTP_201_CREATED)