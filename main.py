import flet as ft
import renombrar_imagenes

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        # se actualiza el texto del cuadro de texto
        if (e.path != None):
            carpeta_seleccionada.value = e.path
        else:
            carpeta_seleccionada.value = "Cancelado"
        carpeta_seleccionada.update()

    # se crea un selector de archivos
    # se le pasa una función que reciba el enveto de archivos seleccionados
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    
    # se crea un cuadro de texto en la interfaz gráfica
    carpeta_seleccionada = ft.Text()

    page.overlay.append(pick_files_dialog)
    
    def renombrar(x: ft.ControlEvent):
        print("Renombrando imágenes en: " + carpeta_seleccionada.value)
        renombrar_imagenes.renombrar_imagenes(carpeta_seleccionada.value)
        print("Listo, imágenes renombradas en: " + carpeta_seleccionada.value)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Seleccionar carpeta",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.get_directory_path(),
                ),
                carpeta_seleccionada,
                ft.FilledButton("Renombrar", icon=ft.icons.PLAY_CIRCLE_FILL, on_click=renombrar),
            ]
        )
    )

ft.app(main)