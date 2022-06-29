from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import User, Session, Event, Status, EventType, Video, VideoSession
import json

class UserViewSet(ViewSet):
    def create(self, request, pk=None):
        try:
            # Get user data 
            userData = json.loads(request.body)
            userPostId = userData['uid']
            
            # Initial response items
            resUid = userPostId
            resSessionId = None
            resFeed = []

            # Find if uid exists 
            if not userPostId:
                # Register for new user
                newUser = User.objects.create()
                resUid = str(newUser.pk)
            
            # Assign new session id and register
            resSessionId = resUid + '-' + (Session.objects.filter(uid=resUid).count() + 1)
            Session.objects.create(uid=resUid, session_id=resSessionId)

            # Register current user video order and get correspond video information
            resVideoOrder = '1,2,3' #TODO: Make a custom distribute rule
            VideoSession.objects.create(session_id=resSessionId, video_order=resVideoOrder)
            for videoId in resVideoOrder.split(','):
                videoInfo = Video.objects.filter(id=int(videoId)).values()[0]
                resFeed.append(videoInfo)

            # Make Response object
            resData = {
                'uid': resUid,
                'session_id': resSessionId,
                'feed': resFeed
            }
            return Response(json.dumps(resData), status=status.HTTP_200_OK)
            
        except Exception as e: 
            print(e)
            return Response(json.dumps({'res': 'fail', 'detail': 'something wrong happened'}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)









