from django import template
from django.utils import timezone
from app.models import User, Favorite

register = template.Library()

@register.filter(name="relative_time")
def relative_time(posted_time):
    unix_r = int(timezone.now().timestamp()) - int(posted_time.timestamp())
    ret = ""
    #１分
    if unix_r < 60:
        ret = "数秒前"
    #１時間
    elif unix_r < 3600:
        ret = str(unix_r // 60) + "分前"
    #１日
    elif unix_r < 86400:
        ret = str(unix_r // 3600) + "時間前"
    #１週間（７日）
    elif unix_r < 604800:
        ret = str(unix_r // 86400) + "日前"
    #１か月(３０日)
    elif unix_r < 2592000:
        ret = str(unix_r // 604800) + "週間前"
    #１年(３６５日)
    elif unix_r < 31536000:
        ret = str(unix_r // 2592000) + "か月前"
    else:
        ret = str(unix_r // 31536000) + "年前"
    return ret

@register.filter(name="favo_counta")
def favo_counta(id):
    favo_sum = len(Favorite.objects.filter(target=id))
    if favo_sum > 0:
        return favo_sum
    else:
        return ""



@register.filter(name="user_favo")
def user_favo(id, user_name):
    if Favorite.objects.filter(target=id, user=User.objects.get(username=user_name)):
        return "check_heart"
    else:
        return ""