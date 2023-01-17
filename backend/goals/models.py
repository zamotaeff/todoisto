from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)


class Status(models.IntegerChoices):
    to_do = 1, "К выполнению"
    in_progress = 2, "В процессе"
    done = 3, "Выполнено"
    archived = 4, "Архив"


class Priority(models.IntegerChoices):
    low = 1, "Низкий"
    medium = 2, "Средний"
    high = 3, "Высокий"
    critical = 4, "Критический"


class GoalCategory(DatesModelMixin):
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(USER_MODEL, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Goal(DatesModelMixin):
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(USER_MODEL, verbose_name="Автор",
                             on_delete=models.PROTECT)
    description = models.TextField(verbose_name="Описание")
    due_date = models.DateTimeField(verbose_name="Дата выполнения")
    status = models.PositiveSmallIntegerField(verbose_name="Статус",
                                              choices=Status.choices,
                                              default=Status.to_do)
    priority = models.PositiveSmallIntegerField(verbose_name="Приоритет",
                                                choices=Priority.choices,
                                                default=Priority.medium)
    category = models.ManyToManyField(GoalCategory,
                                      verbose_name='Категория/Категории')

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"


class GoalComment(DatesModelMixin):
    text = models.TextField(verbose_name="Текст")
    goal = models.ForeignKey(Goal,
                             on_delete=models.PROTECT,
                             verbose_name='Цель',
                             related_name='comments')
    user = models.ForeignKey(USER_MODEL,
                             verbose_name="Автор",
                             on_delete=models.PROTECT,
                             related_name='comments')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
