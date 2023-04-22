from app.models import *


category1 = Category.objects.create(name="продукты")
category2 = Category.objects.create(name="мыломойка")

product1 = Product.objects.create(name="хлеб", price=20)
product2 = Product.objects.create(name="вода", price=45)
product3 = Product.objects.create(name="моющее средство для посуды", price=150)
product4 = Product.objects.create(name="порошок", price=320)
product5 = Product.objects.create(name="шампунь", price=500)
