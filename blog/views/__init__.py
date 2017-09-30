from django.shortcuts import render_to_response


def base(request):
    return render_to_response("base.html", {
        'SITE_ROOT': 'qwe'
    })
