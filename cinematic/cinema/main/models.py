from django.db import models

# Create your models here.

class Rate(models.Model): # Возрастной рейтинг
    rate = models.CharField(max_length=3,verbose_name='Возрастной рейтинг',help_text='Введите возрастной рейтинг')

    def as_json(self):
        
        return dict(
            rate=self.rate
        )

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
        
    def __str__(self) -> str:
        return f'{self.rate}'

class Genre(models.Model): # Жанр
    name_genre = models.CharField(max_length=20,verbose_name='Жанр',help_text='Введите жанр')
    
    def as_json(self):
        
        return dict(
            name_genre=self.name_genre
        )
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        
    def __str__(self) -> str:
        return f'{self.name_genre}'

class Film (models.Model): # Фильм
    name_film = models.CharField(max_length=200,verbose_name="Название фильма",help_text="Введите название фильма")
    date = models.DateField(verbose_name="Дата выхода",help_text="Введите дату выхода",null=True,blank=True)
    duration = models.CharField(max_length=12,verbose_name='Продожительность',help_text='Введите продолжительность фильма',null=True,blank=True)
    rate = models.ForeignKey('Rate',on_delete=models.CASCADE,verbose_name="Рейтинг",help_text='Выберите рейтинг',null=True,blank=True)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE,verbose_name='Жанры',help_text='Выберите жанры',null=True,blank=True)
    description = models.CharField(max_length=1000,verbose_name="Описание",help_text="Введите описание фильма")
    
    def as_json(self):    
        return dict(
            name_film=self.name_film,
            date=self.date.strftime('%Y-%m-%d'),
            duration=self.duration,
            rate=self.rate.as_json(),
            genre=self.genre.as_json(),
            description=self.description
        )
    class Meta:
        ordering = ['date','name_film']
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        
    def __str__(self) -> str:
        return f'{self.name_film}'
    
class Hall (models.Model): # Зал
    name_hall = models.CharField(max_length=30,verbose_name='Зал',help_text='Введите название зала')
    capacity = models.IntegerField(verbose_name='Вместимость',help_text='Введите вместимость')
    
    def as_json(self):        
        return dict(
            name_hall=self.name_hall,
            capacity=self.capacity
        )
    
    class Meta:
        ordering = ['name_hall','capacity']
        verbose_name = "Зал"
        verbose_name_plural = "Залы"
        
    def __str__(self) -> str:
        return f'{self.name_hall}'
    
class Price (models.Model): # Цена
    name_price = models.CharField(max_length=100, verbose_name='Тип билета',help_text='Введите тип билета')
    price = models.IntegerField(verbose_name='Цена',help_text='Введите цену')
    
    def as_json(self):        
        return dict(
            name_price=self.name_price,
            price=self.price
        )
    class Meta:
        ordering = ['name_price','price']
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        
    def __str__(self) -> str:
        return f'{self.name_price} - {self.price}'
    
class Seans (models.Model): # Сеанс
    film = models.ForeignKey('Film',on_delete=models.CASCADE,verbose_name='Фильм',help_text='Выберите фильм')
    hall = models.ForeignKey('Hall',on_delete=models.CASCADE,verbose_name='Зал',help_text='Выберите зал')
    date = models.DateField(verbose_name="Дата cеанса",help_text="Введите дату сеанса",null=True,blank=True)
    time_begin = models.TimeField(verbose_name="Время начала сеанса",help_text="Введите время начала сеанса",null=True,blank=True)
    time_end = models.TimeField(verbose_name="Время окончания сеанса",help_text="Введите Время окончания сеанса",null=True,blank=True)
    price_seans = models.ForeignKey('Price',on_delete=models.CASCADE,verbose_name='Обычная цена за сеанс',help_text='Введите цену за сеанс',default=3)
    status = models.BooleanField(verbose_name='Зал заполнен?',default=False)
    
    def as_json(self):    
        return dict(
            film=self.film.as_json(),
            hall=self.hall.as_json(),
            date=self.date.strftime('%Y-%m-%d'),
            time_begin=self.time_begin.strftime('%H:%M:%S'),
            time_end=self.time_end.strftime('%H:%M:%S'),
            price_seans=self.price_seans.as_json(),
            status=self.status
        )
    
    class Meta:
        ordering = ['date','time_begin','film']
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"
        
    def __str__(self) -> str:
        return f'{self.film} - {self.hall} - {self.date} - {self.time_begin} - {self.status}'
    
class Ticket (models.Model):
    seans = models.ForeignKey('Seans',on_delete=models.CASCADE,verbose_name='Сеанс',help_text='Выберите сеанс')
    price =  models.ForeignKey('Price',on_delete=models.CASCADE,verbose_name='Цена за сеанс',help_text='Выберите цену за сеанс',default=3)
    
    def as_json(self):    
        return dict(
            seans=self.seans.as_json(),
            price=self.price
        )
    class Meta:
        ordering = ['seans','price']
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"
        
    def __str__(self) -> str:
        return f'{self.seans} - {self.price}'