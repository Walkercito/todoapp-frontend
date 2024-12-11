import reflex as rx

from todoapp_frontend.styles.styles import Size
from todoapp_frontend.styles.styles import Color
from todoapp_frontend.styles.styles import TextColor


def dashboard_view() -> rx.Component:
    return rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.heading(
                        "Dashboard",
                        color = TextColor.PRIMARY.value,
                        font_size = rx.breakpoints(
                            initial = "xl",
                            sm = "2xl",
                            lg = "3xl"
                        )
                    ),
                    rx.text(
                        "Welcome to your dashboard!",
                        color = TextColor.SECONDARY.value,
                        font_size = rx.breakpoints(
                            initial = "sm",
                            sm = "md",
                            lg = "lg"
                        )
                    ),
                    spacing = Size.DEFAULT.value,
                    align = "center",
                ),
                height = "auto",
                width = rx.breakpoints(
                    initial = "100%",
                    sm = "80%",
                    lg = Size.CARD_WIDTH.value
                ),
                border_radius = Size.MEDIUM.value,
                padding = rx.breakpoints(
                    initial = "4",
                    sm = "8",
                    lg = Size.EXTRA_LARGE.value
                ),
            )
        ),
        center_content = True,
        size = "2"
    )