"""
Landing page controller var miscellaneous pages.
"""
from flask import render_template


def create_landing_page_routes(app):

    @app.route('/')
    def root():
        return 'Hello from BeamIt!!'

    @app.route('/android/download')
    def android_download():
        return render_template('androidAppDownload.html')
