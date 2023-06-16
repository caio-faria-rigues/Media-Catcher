import flet as ft
import math

class MediaCatcher(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.page.title = "Media Catcher"
        self.page.window_width = 1000
        self.page.window_height = 600
        self.page.window_resizable = False
        self.page.window_maximizable = False

        self.page.add(
            ft.Container(
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.bottom_left,
                    end=ft.alignment.top_right,
                    colors=[
                        "#001147",
                        "#180837",
                        "#180837"
                    ],
                    tile_mode=ft.GradientTileMode.MIRROR,
                    rotation=math.pi / 3
                ),
                width=1000,
                height=600,
                margin=-10,
                content=ft.Row(
                    [
                        ft.Container(
                            expand=False,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#001147",
                                    "#180837"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left
                            ),
                            width=250,
                            height=500,
                            border_radius=20,
                            margin=15,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=ft.colors.BLACK45,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            )
                        ),
                        ft.Container(
                            expand=False,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                colors=[
                                    "#001147",
                                    "#180837"
                                ],
                                begin=ft.alignment.top_right,
                                end=ft.alignment.bottom_left
                            ),
                            width=665,
                            height=500,
                            border_radius=20,
                            margin=15,
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=ft.colors.BLACK45,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            )
                        )
                    ],
                    alignment=ft.alignment.center
                )
            )
        )

        self.page.add(
            ft.Container(
                expand=True,
                alignment=ft.alignment.center_left,
                gradient=ft.RadialGradient(
                    colors=[
                        "#001147",
                        "#180837"
                    ]
                ),
                width=150,
                height=150,
                border_radius=5

            )
        )
        self.page.update()


ft.app(target=MediaCatcher)
