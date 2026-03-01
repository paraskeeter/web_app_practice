from nicegui import app, ui
from components.dashboard import Dashboard
from components.graph import graph

class Home:
    def __init__(self):
        self.model = None
    
    def create(self) -> None:
        @ui.page('/')
        def home():
            Dashboard().render(current_page='/')  # just this line
            ui.label('Home page')

            with ui.column().classes('absolute-center items-center w-full'):
                ui.label(f'Hello {app.storage.user["username"]}')
                # Line chart
                graph(
                    title='Monthly Sales',
                    x=['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                    y=[12, 19, 8, 25, 30],
                    kind='line',
                    x_label='Month',
                    y_label='Sales',
                )

                # Bar chart
                graph(
                    title='User Signups',
                    x=['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                    y=[5, 14, 9, 22],
                    kind='bar',
                    color='#E45B5B',
                )