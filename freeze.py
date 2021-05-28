#!/usr/bin/env python

from website import app, flatpages
from utils import compile_css
from flask_frozen import Freezer
from flask import url_for
from images import hash_dir_filenames, upload_images
import http.server as svr
import os

freezer = Freezer(app)
# app.config["FREEZER_DESTINATION_IGNORE"] = 'website/build/static/css/*'
# app.config["FREEZER_STATIC_IGNORE"] = 'website/static/css/*'

# Manually add fonts to list to incorporate into freezer
FONTS = {
'Roboto_Slab' : 'RobotoSlab-VariableFont_wght-Latin.woff2', #tuple: vf, latin, woff2
'Public_Sans' : 'PublicSans-VariableFont_wght-Min.woff2'
}

# Instructs the freezer to also check for dynamically generated urls from serve_page functinon.
@freezer.register_generator
def fonts():
    print('Registering Font files:')
    for dir, font in FONTS.items():
        path = os.path.join('fonts', dir, font)
        print(path)
        yield url_for('static', filename=path)


if __name__ == '__main__':
    print("Building website:")

    # TODO: check font files exist and compile with pyftsubset

    # Freeze static files into default directory 'build'
    freezer.freeze()
    print("Website frozen")

    # TODO: compile scss with sass commandline: here or in run?
    compile_css('website/static/scss', 'website/build/static/css', compressed=True)
    print("Css recompiled")

    # If dir hash has changed, upload images:
    if hash_dir_filenames('website/static/img/out', 'hash.txt'):
        upload_images('website/static/img/out')
    else:
        print('No new images to upload')

    # Use python builtin server to serve static files based on directory structure
    os.chdir('website/build')
    svr.test(HandlerClass=svr.SimpleHTTPRequestHandler, port=5001)