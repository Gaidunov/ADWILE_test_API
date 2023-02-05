from django.contrib import admin
from .models import Teaser, Wallet

@admin.register(Teaser)
class TeaserAdmin(admin.ModelAdmin):
    pass 

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass 
# Register your models here.
