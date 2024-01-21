# firstapp/models.py
from django.db import models

class Message(models.Model):
    sender_name = models.CharField(max_length=50)
    receiver_name = models.CharField(max_length=50)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_name} to {self.receiver_name}: {self.message_content}"
