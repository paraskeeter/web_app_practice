from nicegui import ui, app

class Dashboard:

    def render(self, current_page: str = '') -> None:
        with ui.left_drawer().classes('bg-gray-800 text-white'):
            ui.label('My App').classes('text-xl font-bold p-4')
            ui.separator()

            nav_items = [
                ('Home', '/', 'home'),
                ('Settings', '/settings', 'settings'),
                ('BIT', '/diagnostics', 'health_and_safety'),
                ('Log', '/logging', 'article'),
            ]

            # for label, route, icon in nav_items:
            #     with ui.item(on_click=lambda r=route: ui.navigate.to(r)).classes(
            #         'bg-gray-700' if current_page == route else ''
            #     ):
            #         ui.icon(icon)
            #         ui.label(label)
            for label, route, icon in nav_items:
                is_active = current_page == route
                # ui.link handles navigation natively in the browser — no Python roundtrip
                with ui.link(target=route).classes('no-underline w-full'):
                    with ui.row().classes(
                        f'items-center gap-2 px-4 py-2 rounded cursor-pointer '
                        f'{"bg-gray-700" if is_active else "hover:bg-gray-600"}'
                    ):
                        ui.icon(icon).classes('text-white')
                        ui.label(label).classes('text-white')

        with ui.header().classes('bg-gray-900 text-white justify-between'):
            ui.label(f'Welcome, {app.storage.user.get("username", "User")}')
            ui.button('Logout', on_click=self._logout).classes('bg-red-600')

    def _logout(self):
        app.storage.user['authenticated'] = False
        ui.navigate.to('/login')