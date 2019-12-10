from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class OrderField(models.PositiveIntegerField):  # 3
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):  # 4
        if getattr(model_instance, self.attname) is None:  # 5
            try:
                qs = self.model.objects.all()  # 6
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}  # 7
                    qs = qs.filter(**query)  # 8
                last_item = qs.latest(self.attname)  # 9
                value = last_item.order + 1  # 10
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)  # 11
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)
