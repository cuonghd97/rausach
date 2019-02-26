from django.urls import path
from . import views

app_name = "ManageStore"

urlpatterns = [
  path('', views.Direct),
  path('login/', views.LoginClass.as_view(), name="login"),
  path('base/', views.Base, name='base'),
  path('logout/', views.UserLogout, name="logout"),
  path('dashboard/', views.Dashboard, name='dashboard'),
  # Products
  path('products/list', views.products, name='products'),
  path('products/set-price/', views.set_price, name='set_price'),
  path('products/inventory/', views.inventory, name='inventory'),
  # Exchange
  path('exchange/invoices/', views.invoice, name='invoices'),
  path('exchange/purchase-order/', views.purchase_order, name='purchase_order'),
  path('exchange/purchase-return/', views.pruchase_return, name='purchase_return'),
  path('exchange/returns/', views.returns, name='returns'),
  path('exchange/damage-item/', views.damage_item, name='damage_item'),
  # Cash book
  path('cash-book/', views.cash_book, name='cash_book'),
  # Partner
  path('partner/customers/', views.customers, name='customers'),
  path('partner/suppliers/', views.suppliers, name='suppliers'),
  # Reports
  path('report/customer-report/', views.customer_report, name='customer_report'),
  path('report/employee-report/', views.employee_report, name='employee_report'),
  path('report/end-of-day-report/', views.end_of_day_report, name='end_of_day_report'),
  path('report/order-report/', views.order_report, name='order_report'),
  path('report/product-report/', views.product_report, name='product_report'),
  path('report/sale-report/', views.sale_report, name='sale_report'),
  path('report/supplier-report/', views.supplier_report, name='supplier_report')
]