from django.db.models import Q
from apps.core.models import Contact


def get_filtered_contacts(params):
    keyword = params.get('keyword')
    gender = params.get('gender')
    category = params.get('category')
    created_at = params.get('created_at')

    contacts = Contact.objects.all().order_by('-created_at')

    if keyword:
        contacts = contacts.filter(
            Q(last_name__icontains=keyword)|
            Q(first_name__icontains=keyword)|
            Q(email__icontains=keyword)
        )


    if gender:
        contacts = contacts.filter(gender=gender)


    if category:
        contacts = contacts.filter(category=category)


    if created_at:
        contacts = contacts.filter(created_at__date=created_at)

    return contacts