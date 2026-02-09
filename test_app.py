import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Remove any conflicting 'app' from sys.modules if present
if 'app' in sys.modules:
    del sys.modules['app']

# Import local app.py as a module
import importlib.util
spec = importlib.util.spec_from_file_location("myapp", "data/app.py")
myapp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(myapp)

import dash
from dash import dcc, html

def test_header_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = myapp.create_layout()

    header = None
    for component in dash_app.layout.children:
        if isinstance(component, html.H1):
            header = component
            break
    assert header is not None
    assert header.children == "Pink Morsel Sales Visualizer"

def test_visualization_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = myapp.create_layout()

    graph = None
    for component in dash_app.layout.children:
        if isinstance(component, dcc.Graph):
            graph = component
            break
    assert graph is not None

def test_region_picker_present():
    dash_app = dash.Dash(__name__)
    dash_app.layout = myapp.create_layout()

    radio = None
    for component in dash_app.layout.children:
        if isinstance(component, html.Div):
            for child in component.children:
                if isinstance(child, dcc.RadioItems):
                    radio = child
                    break
        if radio:
            break
    assert radio is not None
    assert len(radio.options) == 5

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])