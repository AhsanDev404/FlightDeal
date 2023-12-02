from django.contrib import admin
from .models import SignUp, SignUpAd, SignUpMod, LogIn, DealInfo, Msg, AdReview

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ("id", "fname", "lname", "uname", "email", "pw", "dob", "usi", "join_date")

class AdvAdmin(admin.ModelAdmin):
	list_display = ("id", "bname", "abn", "uname", "email", "pw", "join_date")

class ModAdmin(admin.ModelAdmin):
	list_display = ("id", "fname", "lname", "uname", "email", "pw", "join_date")

class LogInAdmin(admin.ModelAdmin):
	list_display = ("id", "email", "pw")

class DealInfoAdmin(admin.ModelAdmin):
	list_display = ("id", "ad_desc", "start_date", "end_date", "airline", "disc_price", "price", "acc")

class MsgAdmin(admin.ModelAdmin):
	list_display = ("id", "uname", "recipient", "date_sent")

class ReviewAdmin(admin.ModelAdmin):
	list_display = ("id", "mod_uname", "ad_uname", "approve", "feedback", "date")


admin.site.register(SignUp, StudentAdmin)
admin.site.register(SignUpAd, AdvAdmin)
admin.site.register(SignUpMod, ModAdmin)
admin.site.register(LogIn, LogInAdmin)
admin.site.register(DealInfo, DealInfoAdmin)
admin.site.register(Msg, MsgAdmin)
admin.site.register(AdReview, ReviewAdmin)