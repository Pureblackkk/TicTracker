from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)

class Session(models.Model):
    uid = models.ForeignKey(User, related_name='uid_session', on_delete=models.CASCADE)
    session_id = models.CharField(max_length=50, null=False)
    register_time = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey(Session, related_name='session_event', on_delete=models.CASCADE)
    event_type = models.IntegerField(null=False)
    video_id = models.IntegerField(null=False)
    video_time = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey(Session, related_name='session_event', on_delete=models.CASCADE)
    status_description = models.CharField(max_length=5000, null=True) # May need to modify to specific fields

class EventType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_description = models.CharField(max_length=1000, null=False)

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.IntegerField(null=False)
    type = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    music = models.CharField(max_length=100, null=False)
    tags = models.CharField(max_length=1000, null=False)
    likes = models.IntegerField(null=False)
    comments = models.IntegerField(null=False)

class VideoSession(models.Model):
    session_id = models.ForeignKey(Session, related_name='session_video', on_delete=models.CASCADE)
    video_order = models.CharField(max_length=1000, null=False)

    


