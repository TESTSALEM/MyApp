[app]
# اسم التطبيق الذي يظهر للمستخدم
title = MyApp

# اسم الحزمة (يجب أن يكون بدون مسافات)
package.name = myapp

# اسم الحزمة على أندرويد (لا تغيره إن لم تعرف ماذا تفعل)
package.domain = org.test

# ملف البداية الرئيسي في مشروعك
source.main = main.py

# مجلد المشروع
source.dir = .

# الصيغ التي سيتم تضمينها داخل الـ APK
source.include_exts = py,png,jpg,kv

# لا توجد أيقونة وصورة بداية → نوقفهم
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

# النسخة
version = 1.0

# الواجهة تعتمد على Kivy
requirements = python3, kivy

# لغة واجهة المستخدم
fullscreen = 0

# اتجاه التطبيق (عمودي)
orientation = portrait

# تفعيل log لعرض الأخطاء
log_level = 2


[buildozer]
log_level = 2


[android]
# المعمارية المدعومة
android.archs = arm64-v8a, armeabi-v7a

# نسخة Android API المستخدمة
android.api = 31

# أقل نسخة أندرويد يدعمها التطبيق
android.minapi = 21

# NDK نسخة مناسبة لـ Android API 31
android.ndk = 25b

# SDK المناسب
android.sdk = 31

# نوع الحزمة النهائية
android.packaging_mode = aab

# تشغيل الإنترنت داخل التطبيق إن احتجت لاحقًا
android.permissions = INTERNET


[python]
# لا تغيرها
android.accept_sdk_license = True
