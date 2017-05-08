from django.db import models


# Create your models here.

class Blog(models.Model):
    """
    博客
    """

    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('文章内容')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

