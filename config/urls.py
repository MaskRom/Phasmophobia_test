from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from app import views

from django.conf import settings
from django.conf.urls.static import static


# 実はページを表示するだけならこのように1行で書くことが出来ます。
"""
index_view = TemplateView.as_view(template_name="registration/index.html")
"""

urlpatterns = [
    path('admin/', admin.site.urls),

    # login_requiredで囲むとログイン必須のページになります。
    path("", login_required(views.index_view.as_view()), name="index"),
    # この１行でdjangoでデフォルトで用意している以下がすべて入ります。
    # ・ログイン
    # ・ログアウト
    # ・パスワード変更
    # ・パスワード再発行
    path('', include("django.contrib.auth.urls")),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
    path('like/', views.like, name='like'),

    path('post/', views.post_view.as_view(), name='post_create')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)