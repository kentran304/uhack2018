from webapp.models import Customer

def create_user_by_type(backend, user, request, response, *args, **kwargs):
    if request['user_type'] == "customer" and not Customer.objects.filter(user_id=user.id):
        Customer.objects.create(user_id=user.id, avatar = avatar)