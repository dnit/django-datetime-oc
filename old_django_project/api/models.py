from django.db import models


# Create your models here.

class DBManager(models.Manager):
    def with_raw(self):
        query = """
            SELECT id, first_field , NOW() AS curr_time from dummy
        """
        return self.raw(query)


class Dummy(models.Model):
    first_field = models.DateTimeField(auto_now_add=True)

    objects = DBManager()

    class Meta:
        db_table = 'dummy'

    def __init__(self, *args, **kwargs):
        self.curr_time = kwargs.pop('curr_time', None)
        super(Dummy, self).__init__(*args, **kwargs)

    @property
    def is_valid(self):
        if self.curr_time:
            return self.first_field < self.curr_time
