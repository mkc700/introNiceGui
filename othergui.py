from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz Click aqui', on_click=lambda: ui.notify('Gracias!'))
with ui.row():
    ui.checkbox('Estas de Acuerdo? ', on_change=show)
    ui.switch('Modo', on_change=show)
ui.radio(['Hombre', 'Mujer', 'Un tipo de gay'], on_change=show).props('inline')
with ui.row():
    ui.input('Inserta texto aqui', on_change=show)
    ui.select(['Monterrey', 'Cruz azul', 'Tigres', 'Toluca', 'Chivas'], on_change=show)
ui.link('And many more...', '/documentation').style('font-size: 3em;color: red;margin-left:8em;')

ui.run()