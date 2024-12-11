import reflex as rx

from todoapp_frontend.styles.styles import Color
from todoapp_frontend.styles.styles import TextColor
from todoapp_frontend.styles.styles import Size

def login_view() -> rx.Component:
    return rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.box(
                        rx.center(
                            rx.icon(
                                tag = "circle-check",
                                size = 48,
                                color = Color.ICON.value
                            )
                        )
                    ),
                    rx.box(
                        rx.center(
                            rx.vstack(
                                rx.heading(
                                    "Todo APP",
                                    color = TextColor.PRIMARY.value,
                                    font_size = rx.breakpoints(
                                        initial = "xl",
                                        sm = "2xl",
                                        lg = "3xl"
                                    )
                                ),
                                rx.text(
                                    "Organiza tus tareas de manera eficiente",
                                    color = TextColor.SECONDARY.value,
                                    font_size = rx.breakpoints(
                                        initial = "sm",
                                        sm = "md",
                                        lg = "lg"
                                    )
                                ),
                                align = "center",
                                spacing = "1"
                            ),
                        ),
                    ),
                    rx.vstack(
                        rx.input(
                            rx.input.slot(
                                rx.icon(
                                    tag = "mail",
                                    color = Color.ICON.value
                                )
                            ),
                            placeholder = "Correo electrónico",
                            width = "100%"
                        ),
                        rx.input(
                            rx.input.slot(
                                rx.icon(
                                    tag = "lock",
                                    color = Color.ICON.value
                                )
                            ),
                            placeholder = "Contraseña",
                            type = "password",
                            width = "100%"
                        ),
                        rx.button(
                            "Iniciar Sesión",
                            width = "100%"
                        ),
                        width = "100%",
                        spacing = Size.DEFAULT.value,
                        padding = rx.breakpoints(
                            initial = "2",
                            sm ="4",
                            lg = "6"
                        ),
                    ),
                    spacing = Size.LARGE.value,
                    align = "center",
                    width = "100%"
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