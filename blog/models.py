from urllib import request
from django.db import models
from django.shortcuts import render


# Create your models here.
class Post(models.Model):
    '''даные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')
    views = models.IntegerField()
   
    

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    email = models.EmailField()
    telefon = models.CharField('Телефон', max_length=100)
    name = models.CharField('Имя', max_length=50)
    text_comment = models.TextField('Текст комментария', max_length=200)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name}, {self.text_comment}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    '''Лайки'''
    ip = models.CharField('IP адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)



class Visit(models.Model):
    ip_addr = models.CharField("Ip", max_length=50)
    count = models.IntegerField(default=0)
    data = models.CharField("Data", max_length=50)

    '''выводит в админку поля обекта'''
    def __str__(self):
        return f'{"IP адрес: "+self.ip_addr+" | | "},{" Количество : "+str(self.count)}, {" | | Дата: "+self.data}'

    class Meta:
        verbose_name = 'Посетители:'
        verbose_name_plural = 'Гости сайта'


   