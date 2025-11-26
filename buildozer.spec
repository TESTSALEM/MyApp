[app]

title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv,mp3,wav,ogg,ttf

version = 1.0

requirements = python3,kivy

presplash.filename = splash.png
fullscreen = 0

orientation = portrait

icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# دعم لمسارات الملفات والصور
android.allow_backup = True
android.hardwareAccelerated = True

# إذا لديك صور بالخلفية ستعمل بدون مشاكل
