[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf
version = 1.0

# Main file
main.py = main.py

# Icon
# icon.filename = icon.png

# Supported orientations: portrait, landscape, all
orientation = portrait

# Fullscreen?
fullscreen = 1

# Permissions example
# android.permissions = INTERNET

# Kivy Requirements
requirements = python3,kivy

# Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# Minimum / Target Android API
android.minapi = 21
android.api = 31

# **CRITICAL FIX**
# Use Android NDK r23b because Kivy does NOT work with 25/26/27+
android.ndk = 23b

# Use default SDK (works with NDK 23b)
android.sdk = 24.1.6392215

# Don't set ndk_path manually, let Buildozer manage it
android.ndk_path =

# Package format: debug or release
buildozer.package_format = apk

log_level = 2


[buildozer]
warn_on_root = 1
