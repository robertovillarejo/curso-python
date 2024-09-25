import flet as ft
import renombrar_imagenes

def main(page: ft.Page):
    page.title = "Renombrado de imágenes"
    page.padding = 50

    def renombrar(x: ft.ControlEvent):
        renombrar_imagenes.renombrar_imagenes(carpeta_seleccionada.value, jpg=ch_jpg.value, png=ch_png.value, gif=ch_gif.value, bmp=ch_bmp.value)
        dlg = ft.AlertDialog(
        title=ft.Text("Listo, imágenes renombradas en: " + carpeta_seleccionada.value))
        page.open(dlg)
    
    def handle_close(e):
        page.close(dlg_modal)
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor confirmar"),
        content=ft.Text("¿Quieres renombrar todas las imágenes?"),
        actions=[
            ft.TextButton("Sí", on_click=renombrar),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        )
    
    #Checkboxes
    ch_jpg=ft.Checkbox(label=".jpg", value=True)
    ch_png=ft.Checkbox(label=".png", value=False)
    ch_gif=ft.Checkbox(label=".gif", value=False)
    ch_bmp=ft.Checkbox(label=".bmp", value=False)

    boton_carpeta = ft.ElevatedButton("Seleccionar carpeta",icon=ft.icons.FOLDER,on_click=lambda _: pick_files_dialog.get_directory_path())
    boton_renombrar = ft.ElevatedButton("Renombrar", on_click=lambda e: page.open(dlg_modal), icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE, disabled=True)

    def pick_files_result(e: ft.FilePickerResultEvent):
        # se actualiza el texto del cuadro de texto
        if (e.path != None):
            carpeta_seleccionada.value = e.path
            boton_renombrar.disabled = False
        else:
            carpeta_seleccionada.value = "Cancelado"
            boton_renombrar.disabled = True
        carpeta_seleccionada.update()
        boton_renombrar.update()

    # se crea un selector de archivos
    # se le pasa una función que reciba el enveto de archivos seleccionados
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    
    # se crea un cuadro de texto en la interfaz gráfica
    carpeta_seleccionada = ft.Text()

    page.overlay.append(pick_files_dialog)
    
    page.add(
        # header
        ft.ResponsiveRow(
            controls=[
                ft.Text("Instrucciones:", text_align=ft.TextAlign.START), 
                ft.Text("Seleccione una carpeta para renombrar las imágenes de los tipos seleccionados con el nombre de la carpeta", width=300)
                ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        # main
        ft.ResponsiveRow(
            controls=[
                # seleccionar carpeta
                ft.ResponsiveRow(controls=
                    [
                    boton_carpeta,
                    carpeta_seleccionada
                ]),
                ft.ResponsiveRow(controls = [
                    ch_jpg,
                    ch_png,
                    ch_gif,
                    ch_bmp,
                ]),
                ft.ResponsiveRow(controls = [
                    boton_renombrar
                ])
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        # footer
        ft.ResponsiveRow(
            controls=[
                ft.Text("Hecho por Marco Antonio y Roberto Villarejo", text_align=ft.TextAlign.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        )

ft.app(main)