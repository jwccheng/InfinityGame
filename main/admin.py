from django.contrib import admin
from django.db import models
from account.models import Account
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.contrib.auth.admin import UserAdmin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from tinymce.widgets import TinyMCE


from .models import History
from .models import LuckyNumber
from .models import LuckyNumberOrders
from .models import WinningNumber
from .models import Product
from .models import Redeem


class AccountDetails(resources.ModelResource):
    class Meta:
        model = Account
        exclude = ('id', )

class AccountAdmin(UserAdmin, ImportExportModelAdmin):
    list_display = ('username', 'account_type')
    search_fields = ('username', 'account_type')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Account, AccountAdmin)

admin.site.register(LuckyNumber)
admin.site.register(LuckyNumberOrders)
admin.site.register(History)
admin.site.register(WinningNumber)
admin.site.register(Product)
admin.site.register(Redeem)

# @admin.register(Package,
#                 Transfer,
#                 Transaction,
#                 Cashback,
#                 Product,
#                 Withdrawal,
#                 CarDetails,
#                 Outlet,
#                 PaymentGateway,
#                 UserCart,
#                 )
class ViewAdmin(ImportExportModelAdmin):
    pass