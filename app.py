from nicegui import ui, app
from pages.home import Home
from pages.login import Login
from pages.settings import Settings
from middleware import auth


if __name__ in {'__main__', '__mp_main__'}:
    auth.create()
    page_1 = Home()
    page_1.create()
    page_2 = Login()
    page_2.create()
    page_3 = Settings()
    page_3.create()
    ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')