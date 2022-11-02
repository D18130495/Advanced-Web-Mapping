from whitenoise import WhiteNoise

from Advanced_Web_Mapping import wsgi

application = wsgi()
application = WhiteNoise(application, root="static")
application.add_files("static", prefix="more-files/")
