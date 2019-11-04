from django.db import models

class Country(models.Model):
    # pass
    # field
    CreateDate=models.DateTimeField('创建时间',name='CreateDate',auto_now_add=True)
    Code=models.CharField('国家编码',max_length=2,blank=False)
    Name=models.CharField('国家名称',max_length=200,blank=False)
    FlagPictureName=models.CharField('国旗图片名称',max_length=200,blank=False)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'tb_Country'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'