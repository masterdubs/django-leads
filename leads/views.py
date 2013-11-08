# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import CreateView

from .models import Register
from .forms import RegisterForm


class IndexView(CreateView):
    """
    This view renders the main page
    """
    template_name = 'leads/index.html'
    model = getattr(settings, 'LEADS_REGISTER_MODEL', Register)
    form_class = getattr(settings, 'LEADS_REGISER_FORM_CLASS', RegisterForm)
