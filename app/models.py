from django.db import models
from django.contrib.auth.models import AbstractUser
from auction import settings
from django.contrib.auth import get_user_model

class User(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Баланс счёта', null=True)
    
    def __str__(self):
        return self.username

class Animal(models.Model):

    animal_type = (
        ('ca', u'Кот'),
        ('he', u'Ёж'),
    )
        
    animaltype = models.CharField(max_length=2, choices=animal_type, verbose_name='Вид питомца')
    breed = models.CharField(max_length = 100, verbose_name='Порода питомца')
    name = models.CharField(max_length = 100, verbose_name='Кличка питомца')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner', verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'


class Lot(models.Model):
    animal = models.ForeignKey(Animal, related_name='animal', verbose_name='Питомец', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена лота')

    def __str__(self):
        return '{} - {}'.format(self.animal, self.price)

    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'


class Bid(models.Model):
    lot = models.ForeignKey(Lot, verbose_name='Лот', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Значение ставки')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор ставки', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} ({})'.format(self.author, self.lot, self.value)

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

    def bid_accept(self, pk):
        bid = Bid.objects.get(pk=pk)
        lot = Lot.objects.get(pk=bid.lot_id)
        animal = Animal.objects.get(pk=lot.animal_id)
        User = get_user_model()
        lotauthor = User.objects.get(pk=animal.owner_id)
        bidauthor = User.objects.get(pk=bid.author_id)
        animal.owner_id = bidauthor.id
        bidauthor.balance -= bid.value
        lotauthor.balance += bid.value
        lot.delete()
        animal.save()
        bidauthor.save()
        lotauthor.save()