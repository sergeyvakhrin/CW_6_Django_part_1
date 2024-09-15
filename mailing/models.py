from django.db import models

NULLABLE = {"null": True, "blank": True}


class Message(models.Model):
    """ Класс для модели Сообщения """
    title = models.CharField(max_length=100, default="Рассылка", verbose_name="Заголовок", help_text="Введите заголовок")
    message = models.TextField(verbose_name="Сообщение", help_text="Введите текс")
    image = models.ImageField(upload_to="blog/", verbose_name="Фото", **NULLABLE, help_text="Загрузите фото")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.title}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ("title",)


class Client(models.Model):
    """ Класс для модели Клиент """
    email = models.CharField(max_length=100, verbose_name="Почта для рассылки", help_text='Заполните почту для рассылки')
    name = models.CharField(max_length=100, verbose_name="ФИО", help_text="Введите имя клиента", **NULLABLE)
    comment = models.TextField(verbose_name="Комментарий", help_text="Добавьте комментарий", **NULLABLE)

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ("name",)


class Mailing(models.Model):
    """ Класс для модели Рассылки """
    date_of_first_dispatch = models.DateTimeField(verbose_name="Дата первой отправки", **NULLABLE)
    periodicity = models.CharField(max_length=1, choices={"D": "Раз в день", "W": "Раз в неделю", "M": "Раз в месяц"}, verbose_name="Периодичность отправки", help_text="Выберите периодичность отправки", **NULLABLE)
    status = models.CharField(max_length=20, choices={"C": "Создана", "W": "Запущена", "F": "Завершена"}, verbose_name="Статус рассылки")
    datetime_to_start = models.DateTimeField(verbose_name="Когда нужно разослать?", **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Дата создания рассылки", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Дата изменения рассылки", auto_now=True)
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", help_text="Выберите сообщение", related_name='Mailing')
    client_list = models.ManyToManyField(Client, verbose_name='Клиенты', help_text='Выберите клиентов для рассылки', related_name='Client')

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("status",)


class Attempt(models.Model):
    """ Класс для модели Попытки """
    date_first_attempt = models.DateTimeField(verbose_name="Дата первой попытки", auto_now_add=True)
    date_last_attempt = models.DateTimeField(verbose_name="Дата последней попытки", auto_now=True)
    status = models.BooleanField(verbose_name="Статус рассылки")
    server_response = models.CharField(max_length=50, verbose_name="Ответ сервера")
    mailing_id = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка", help_text="Выберите рассылку", related_name='Attempt')

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.date_last_attempt}"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ("status",)
