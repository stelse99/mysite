from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.subject + " " + self.content + " " + self.create_date.strftime("%Y-%m-%d %H:%M:%S")
    # from django.utils import timezone, dateformat
    # dateformat.format(timezone.now(), 'Y-m-d h:m:s')
    # 1. %-formatting
    # 2. str.format() example: {[field_name]![repr(),str(),asc()]}   ==> {0!s}, {name!r} {!a}
    # 3. str.Template()
    # 4. f-string
    def __repr__(self):
        return (
                self.__class__.__qualname__ + f"(subject={self.subject!r}, content={self.content!r}, "
                                              f"create_date={self.create_date})"
        )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name="상품명")
    price = models.IntegerField(verbose_name="상품가격")
    qty = models.IntegerField(verbose_name="상품수량")
    create_date = models.DateTimeField(verbose_name="생성일시")

    def __str__(self):
        return self.name + " " + str(self.price) + " " + str(self.qty) + " " + self.create_date.strftime(
            "%Y-%m-%d %H:%M:%S")
