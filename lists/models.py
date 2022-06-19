# 它的⼯作是根据models.py⽂件所做的更改，
# 使您能够添加和删除表和列。
# 你可以把它看做数据库的版本控制系统。
from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None)
    #pass
# Create your models here.
