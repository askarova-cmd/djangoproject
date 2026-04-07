from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Dish(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание блюда')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name='Фото блюда')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='dishes', verbose_name='Категория')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"{self.name} - {self.email}"


class Booking(models.Model):
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Номер телефона", max_length=20)
    date = models.DateField("Дата")
    time = models.TimeField("Время")

    PEOPLE_CHOICES = [
        (1, "1 человек"),
        (2, "2 человека"),
        (3, "3 человека"),
        (4, "4 человека"),
        (5, "5+ человек"),
    ]
    people_count = models.IntegerField("Количество людей", choices=PEOPLE_CHOICES)

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"


class BlogPost(models.Model):
    title = models.CharField("Название статьи", max_length=200)
    content = models.TextField("Содержание")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, verbose_name="Статья", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField("Изображение", upload_to='blog_images/')

    def __str__(self):
        return f"Изображение для {self.post.title}"


