from cx_Freeze import setup, Executable

setup(
    name='Kun.uz ',
    version='1.0',
    author='Elchin',
    description='Kun.uz viloyatlar nomi',
    executables=[Executable('main.py',
                            icon='chinese_kuaishou_logo_icon_259360.ico',
                            shortcut_name='kun.uz',
                            shortcut_dir='DesktopFolder')

                 ]
)
