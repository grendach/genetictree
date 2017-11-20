from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class Currency(models.Model):
    currency_name = models.CharField(max_length=50)
    currency_country = models.FileField()
    currency_code = models.CharField(max_length=10)
    currency_symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.currency_code


class Income(models.Model):
    income_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    income_date = models.DateField("Date", default=None)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.income_category) + ' - ' + str(self.income_date)

    def get_absolute_url(self):
        return reverse('grendachwallet:income', kwargs={'pk': self.pk})


class Expense(models.Model):
    expense_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    expense_date = models.DateField("Date", default=None)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.expense_category) + ' - ' + str(self.expense_date)

    def get_absolute_url(self):
        return reverse('grendachwallet:expense')