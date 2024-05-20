# handlers.py

from flask import render_template,request,Blueprint


error_pages=Blueprint('error_pages',__name__)


@error_pages.app_errorhandler(404)
def error_404(error):
    # note that we set the 404 status explicitly
    return render_template('error_pages/404.html'),404


@error_pages.app_errorhandler(403)
def error_403(error):
    # note that we set the 403 status explicitly
    return render_template('error_pages/403.html'),403