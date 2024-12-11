import reflex as rx

from todoapp_frontend.components.navbar import navbar
from todoapp_frontend.pages.login_page import login_page

from todoapp_frontend.styles.styles import MAX_WIDTH
from todoapp_frontend.styles.styles import Color
from todoapp_frontend.styles.styles import Size
from todoapp_frontend.styles.styles import BASE_STYLE


def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.center(
                login_page(),
                width = "100%",
                height = "100vh",
                align = "center",
                justify = "center",
            ),
            width = "100%",
            align = "center",
            justify = "center",
        ),
        align = "center",
        justify = "center",
        bg = Color.BACKGROUND.value,
        width = "100%",
        height = "100vh",  
    )


app = rx.App(
    style = BASE_STYLE
)
app.add_page(index)