from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visibilidad', value=True)
ui.label("idea de posiciones con un dezlizador").style('font-size: 2rem;')
with ui.column().bind_visibility_from(v, 'valores').style("padding: 8em;"):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'primero', 2: 'segundo', 3: 'tercero'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()