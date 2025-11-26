[app]
title = MyApp
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.ndk = 23b
