[app]

# App Info
title = InstaFollowers
package.name = instafollowers
package.domain = org.kivy
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,atlas,zip,html
version = 1.0

# Main Python file
entrypoint = main.py

# Android-specific
requirements = python3,kivy,kivymd,bs4,requests,android
android.permissions = INTERNET
android.api = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21

# Orientation and fullscreen
orientation = portrait
fullscreen = 0

# Icon (optional)
# icon.filename = %(source.dir)s/icon.png

# Presplash (optional)
# presplash.filename = %(source.dir)s/splash.png

# Use this to include additional files inside APK
# android.include = assets:assets

# Package format
android.packaging = apk

# Java / JDK config
android.sdk_path = 
android.ndk_path = 
android.gradle_dependencies = 

# (Optional) Keep original Python source
# keep_python_source = 1

# Logcat options
log_level = 2

[buildozer]

# Log Level
log_level = 2

# Command to run after build (optional)
# post_build_cmds = 

