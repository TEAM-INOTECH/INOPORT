from django.db import models

class Truck(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    reg_number = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()
    maintenance_history = models.TextField(blank=True)
    def __str__(self):
      return self.name + ' (' + self.reg_number + ')'

EMPLOYEE =( ("1", "DRIVER"), ("2", "LABOUR"), ("3", "SUPPLIYER"), ("4","OTHER"))
class Contact_Detail(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    Role = models.CharField(max_length=15,choices = EMPLOYEE, default = '4')
    address = models.TextField(blank=True)
    def __str__(self):
      return self.name

class Material(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
      return self.name
    
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    billing_information = models.TextField(blank=True)
    information = models.TextField(blank=True)
    def __str__(self):
      return self.name 

CHOICES = ( ("1", "COMPLETED"), ("2", "PENDING"))

class Agreement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    topic = models.CharField(max_length=255)
    detail = models.TextField()
    agreement_file = models.FileField(upload_to='media/agreements/', blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      name = f"{self.topic}_{self.customer}" 
      return name
        
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.SET_NULL, null=True)
    delivery_location = models.CharField(max_length=100)
    delivery_date = models.DateTimeField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    paymentdone = models.CharField(max_length=15,choices = CHOICES, default = '1')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    amount_pending = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
   
    def __str__(self):
      orderid = f"{self.customer}_{self.delivery_date}_{self.material}"
      return orderid

    def save(self, *args, **kwargs):
      if self.paymentdone == '1' :
        self.amount_paid = self.price
        self.amount_pending = 0
      else:
        self.amount_pending = int(self.price - self.amount_paid)
      super().save(*args, **kwargs)
        
class statistics(models.Model):
    total_amount_pending = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @classmethod
    def calculate_statistics(cls):
        total_amount_pending = Order.objects.filter(paymentdone='2').aggregate(Sum('amount_pending'))['amount_pending__sum'] or 0
        total_sales = Order.objects.filter(paymentdone='1').aggregate(Sum('price'))['price__sum'] or 0
        total_cost = Order.objects.filter(paymentdone='1').aggregate(Sum('material__cost'))['material__cost__sum'] or 0
        total_profit = total_sales - total_cost
        return cls.objects.create(
            total_amount_pending=total_amount_pending,
            total_sales=total_sales,
            total_profit=total_profit)

    def __str__(self):
        return f"Statistics as of {self.total_sales}"
       