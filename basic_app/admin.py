from django.contrib import admin
from basic_app.models import UserProfileInfo, User,Counsellor,n_g_o,rate_organisation

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Counsellor)
admin.site.register(n_g_o)
admin.site.register(rate_organisation)
