from django.core.urlresolvers import reverse, resolve
from django.utils import timezone
from boats_auth import models


def get_next_view_and_url(request):

    next_view = 'logic:estimate_view'
    next_url = reverse(next_view)

    try:
        next_url_candidate = request.GET['next']
        next_view_candiate = resolve(next_url_candidate)
        next_view_candiate = next_view_candiate.view_name

        next_view = next_view_candiate
        next_url = next_url_candidate

    except:
        pass

    return (next_view, next_url)


def register_ip_address(request):

    ip_address = request.META['REMOTE_ADDR']
    now = timezone.now()

    try:
        visiting_ip = models.VisitingIP.objects.get(ip_address=ip_address)
        print('Got visiting ip: {}'.format(visiting_ip))
    except:
        visiting_ip = models.VisitingIP(ip_address=ip_address)
        visiting_ip.save()
        print('Saved visiting ip: {}'.format(visiting_ip))

    now = timezone.now()

    try:
        visiting_date = models.VisitingDate.objects.get(date=now)
        print('Got visiting date: {}'.format(visiting_date))
    except:
        visiting_date = models.VisitingDate(date=now)
        visiting_date.save()
        print('Saved visiting date: {}'.format(visiting_date))

    try:
        visitor = models.Visitor.objects.get(
            visiting_ip=visiting_ip,
            visiting_date=visiting_date)
        print('Got visitor: {}'.format(visitor))

    except models.Visitor.DoesNotExist:
        visitor = models.Visitor(visiting_ip=visiting_ip,
                                 visiting_date=visiting_date)
        visitor.save()
        print('Saved visitor: {}'.format(visitor))
