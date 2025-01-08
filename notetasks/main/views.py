from django.shortcuts import render
from django.views.generic import TemplateView, View


class MainPageView(View):
    template_name = 'mainpage.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

