from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from rembg import remove
import base64

@api_view(['POST'])
def remove_bg(request):
    post_data = json.loads(request.data)
    uploaded_file = post_data['the_image']
    if not uploaded_file:
        return Response({'error': 'No file found in the request.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # You can process the file here if needed
    # For now, let's just echo it back
    file_content_decoded = base64.b64decode(uploaded_file.encode('utf-8'))
    processed_file = remove(file_content_decoded, alpha_matting=True)
    response = {
        'the_image': base64.b64encode(processed_file).decode('utf-8'),
        'msg': 'DONEEEEE'
    }
    return Response(response, status=status.HTTP_200_OK)
