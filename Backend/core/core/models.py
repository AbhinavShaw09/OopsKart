import uuid
from django.db import models

class BaseModel(models.Model):
    '''
        NOTE: This is the base model which will be inherited by all other model
    '''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True # ye true matlab iss model ka koi table nahi banega db me

    def soft_delete(self):
        """Soft delete the object by setting is_deleted to True."""
        self.is_deleted = True
        self.save()

    def restore(self):
        """Restore a soft-deleted object."""
        self.is_deleted = False
        self.save()

    def delete(self, *args, **kwargs):
        """Override delete method to perform a soft delete by default."""
        self.soft_delete()
