import subprocess
from PyQt5.QtCore import QUrl, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

if __name__ == '__main__':
    # Create the PyQt5 application
    app = QApplication([])

    # Create the main window and set its properties
    window = QMainWindow()
    window.setWindowTitle('მომხმარებლის დამატება')
    window.setGeometry(100, 100, 800, 600)  # Set the window size and position

    # Set the window icon
    app.setWindowIcon(QIcon('../static/logo.png'))  # Replace with the path to your icon image

    # Create a tab widget to hold the web browser tabs
    tab_widget = QTabWidget(window)

    # Create the first web browser tab and load the first URL
    tab1 = QWebEngineView()
    tab1.load(QUrl('http://127.0.0.1:5000'))
    tab_widget.addTab(tab1, 'რეგისტრაცია')

    # Create the second web browser tab and load the second URL
    tab2 = QWebEngineView()
    tab2.load(QUrl('http://127.0.0.1:5000/users'))
    tab_widget.addTab(tab2, 'ადმინ პანელი')

    # Add the tab widget to the main window
    window.setCentralWidget(tab_widget)

    # Create a fade-in animation for the tab widget
    animation = QPropertyAnimation(tab_widget, b'windowOpacity')
    animation.setDuration(500)  # Animation duration in milliseconds
    animation.setStartValue(0.0)  # Start with opacity 0 (fully transparent)
    animation.setEndValue(1.0)  # End with opacity 1 (fully visible)
    animation.setEasingCurve(QEasingCurve.InOutQuad)  # Set the easing curve for smooth animation

    # Define a slot to handle tab change event
    def onTabChanged(index):
        # Start the fade-in animation when switching tabs
        animation.start()

    # Connect the tabChanged signal to the onTabChanged slot
    tab_widget.currentChanged.connect(onTabChanged)

    # Show the window and maximize it
    window.showMaximized()

    # Run the PyQt5 event loop
    app.exec_()

    # Terminate the "main.py" and "gui.py" processes
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(tab1.page().profile().page().processId())])
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(tab2.page().profile().page().processId())])
