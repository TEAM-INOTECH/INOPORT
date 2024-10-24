from django.shortcuts import render
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from .models import Truck, Contact_Detail, Material, Customer, Order, statistics


@login_required
def statistics(request):
    pending_orders = Order.objects.filter(paymentdone='2')
    pending_customers = Customer.objects.filter(order__in=pending_orders).distinct()
    
    #Calculate total pending payment
    total_amount_pending = pending_orders.aggregate(Sum('amount_pending'))['amount_pending__sum'] or 0
    orders = Order.objects.filter(paymentdone='1')
    
    total_price = Order.objects.aggregate(Sum('price'))['price__sum'] or 0
    total_cost_price = Order.objects.aggregate(Sum('cost_price'))['cost_price__sum'] or 0
    total_profit = total_price - total_cost_price
    
    # Get top 5 customers by amount spent
    top_5_customers = (Customer.objects.annotate(total_spent=Sum('order__price')).order_by('-total_spent')[:5])

    # Get most selling material
    # most_selling_material_quantity= (Material.objects.annotate(total_quantity=Sum('order__quantity')).order_by('-total_quantity').first())
    
    #most_selling_material = (Material.objects.annotate(total_orders=Count('order')).order_by('-total_orders').first())
    most_selling_materials = (Material.objects.annotate(total_orders=Count('order')).order_by('-total_orders'))
    return render(request, 'stats.html', {'pending_orders': pending_orders,'pending_customers': pending_customers,'total_sales': total_price,'top_5_customers':top_5_customers, 'total_profit': total_profit, 'most_selling_materials':most_selling_materials,'total_amount_pending':total_amount_pending})
