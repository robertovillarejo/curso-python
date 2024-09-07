import flet as ft
import renombrar_imagenes

def main(page: ft.Page):
    def renombrar(x: ft.ControlEvent):
        renombrar_imagenes.renombrar_imagenes(carpeta_seleccionada.value)
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
    
    
    
    
       
    c = ft.Row(controls=[
           boton_carpeta,
           carpeta_seleccionada,
           boton_renombrar,
        ])
    page.add(c)
""""
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
"""
ft.app(main)