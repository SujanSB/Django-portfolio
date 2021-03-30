from django.contrib import admin
from .models import (
    About,
    Service,
    SelectedWorks,
    blogHaru,
    Contact,

)

admin.site.register(SelectedWorks)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(blogHaru)