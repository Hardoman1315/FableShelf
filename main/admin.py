from django.contrib import admin
from main.models import *
from auth_module.models import *
from catalogue_module.models import *


# main module databases
admin.site.register(IndexBanners)

# auth module databases
admin.site.register(CustomUser)

# catalogue module databases
admin.site.register(Categories)
admin.site.register(Authors)
admin.site.register(Books)
