from flask import Flask
from app.controllers.series_cotrollers import series, create, select_by_id


def series_route(app: Flask):
    app.get("/series")(series)
    app.get('/series/<int:serie_id>')(select_by_id)
    app.post("/series")(create)
    
