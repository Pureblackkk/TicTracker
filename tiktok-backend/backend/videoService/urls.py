from rest_framework import routers
import views

# Register url 
VideoServiceRouter = routers.DefaultRouter()
VideoServiceRouter.register(r'video', views.VideoViewSet, 'video')
