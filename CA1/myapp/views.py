from django.http import HttpResponse

def product_view(request, product_id=None):

    if product_id is None:
        return HttpResponse("No valid Product ID supplied.", status=400)

    if product_id.isdigit():
        return HttpResponse(f"Product ID: {product_id}")

    return HttpResponse("Invalid Product ID. Must contain only digits.", status=400)
