from nicegui import ui


def graph(
    title: str = 'Chart',
    x: list = None,
    y: list = None,
    kind: str = 'line',      # 'line', 'bar', 'scatter'
    x_label: str = '',
    y_label: str = '',
    color: str = '#4A90D9',
) -> ui.plotly:
    """Reusable graph component wrapping ui.plotly."""

    x = x or []
    y = y or []

    trace_map = {
        'line':    {'type': 'scatter', 'mode': 'lines+markers'},
        'scatter': {'type': 'scatter', 'mode': 'markers'},
        'bar':     {'type': 'bar'},
    }

    trace = {
        **trace_map.get(kind, trace_map['line']),
        'x': x,
        'y': y,
        'marker': {'color': color},
        'name': title,
    }

    figure = {
        'data': [trace],
        'layout': {
            'title': title,
            'xaxis': {'title': x_label},
            'yaxis': {'title': y_label},
            'margin': {'l': 40, 'r': 20, 't': 40, 'b': 40},
        },
    }

    return ui.plotly(figure).classes('w-full h-64')