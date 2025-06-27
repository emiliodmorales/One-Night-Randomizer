import webbrowser
import os

# Get the absolute path to redirect.html in the current directory
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'redirect.html'))
webbrowser.open(f'file://{file_path}')
