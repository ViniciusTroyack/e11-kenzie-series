from flask import Flask


def init_app(app: Flask):
    from app.routes.series_route import series_route
    series_route(app)
    
    return app
