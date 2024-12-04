from nicegui import ui

ui.icon('thumb_up').style('font-size: 4em; color: #c44949')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML en nice GUI</strong>.')
with ui.row():
    ui.label('Miguel Angel').style('font-size: 5em;color: #5fb371; font-weight: bold; font-family: system-ui, -apple-system, BlinkMacSystemFont,sans-serif;')
    ui.label('Tailwind').style('font-size: 5em;color: #76bcc4;font-style: oblique;')
    ui.label('Quasar').classes('q-ml-xl').style('font-size: 5em;color: #99678a;')

ui.button('NiceGUI on GitHub', on_click=lambda: ui.open('https://github.com/zauberzeug/nicegui')).style('font-size: 2em;background: #5662e3;')
#ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()