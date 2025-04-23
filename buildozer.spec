[app]

# App name and identifiers
title = InstaFollowers
package.name = instafollowers
package.domain = org.kivy

# Source and entry point
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,atlas,zip,html
version = 1.0
entrypoint = main.py

# Orientation and UI
orientation = portrait
fullscreen = 0

# Android requirements
requirements = python3,kivy,kivymd,requests,bs4,android

# Permissions
android.permissions = INTERNET

# Target API & Build Tools
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.archs = armeabi-v7a, arm64-v8a

# Optional: icons and splash
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splash.png

# Include any additional files
# android.include = assets:assets

# Do not compress these extensions
# android.no_compress = assets/

# If needed, keep .py sources in APK
# keep_python_source = 1

# Logcat
log_level = 2

# For Play Store (if planning to publish)
# android.manifest.intent_filters = ...

[buildozer]

# Global log level (0 = error, 2 = info, 1 = warning)
log_level = 2

# Clean before build (recommended)
# clean = true

# Specify build output folder (optional)
# bin_dir = ./bin
