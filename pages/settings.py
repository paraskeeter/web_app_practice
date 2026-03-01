from nicegui import app, ui
from components.dashboard import Dashboard

class Settings:
    def __init__(self):
        pass

    def create(self):
        @ui.page('/settings')
        def settings():
            Dashboard().render(current_page='/settings')  # just this line
            ui.label('Setting page')