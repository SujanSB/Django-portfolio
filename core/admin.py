from django.contrib import admin
from .models import (
    About,
    Service,
    SelectedWorks
)

admin.site.register(SelectedWorks)
admin.site.register(About)
admin.site.register(Service)