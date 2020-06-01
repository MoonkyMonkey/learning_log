from django.db import models

class Topic(models.Model):
    """ 用户学习的主题 """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # py2 中的 __unicode__
    def __str__(self):
        """ 返回模型的字符串表示 """
        return self.text

class Entry(models.Model):
    """ 学到的有关某个主题的具体只是 """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # TODO: on_delete=models.CASCADE
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # TODO: 打错变量名会出现错误, 这个字段的用处
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ 返回模型的字符串表示 """
        if len(self.text) > 50:
            return self.text[:50] + "..."
        return self.text
    
