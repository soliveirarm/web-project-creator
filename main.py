from os import makedirs, getcwd, system, path
import platform

user_system = platform.system()

folder_name = input("Nome da pasta do seu projeto: ")

path = f"./{folder_name}"

try:
    makedirs(path)
    print("Pasta criada!\n")
except FileExistsError:
    folder_exists = input("Essa pasta já existe! Deseja continuar? (s/n) ")
    if folder_exists != "s":
        exit()

js_path = "script.js"
css_path = "style.css"

separate_js_folder = input(
    "Você gostaria de criar uma pasta 'js' para os arquivos javascript? (s/n) "
)

separate_css_folder = input(
    "Você gostaria de criar uma pasta 'css' para os arquivos css? (s/n) "
)

if separate_js_folder == "s":
    makedirs(f"{path}/js")
    js_path = "js/script.js"

if separate_css_folder == "s":
    makedirs(f"{path}/css")
    css_path = "css/style.css"

title = input("Digite o título do seu documento(<title> do seu HTML): ")

with open(f"{path}/index.html", "w") as f:
    f.write(
        f"""<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="stylesheet" href="{css_path}" />
  </head>
  <body>
    <script src="{js_path}"></script>
  </body>
</html>
"""
    )

with open(f"{path}/{css_path}", "w") as f:
    f.write(
        """*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
"""
    )


open(f"{path}/{js_path}", "w")

current_directory = getcwd()

open_with_code = input(
    "\nTudo pronto! Você gostaria de abrir a pasta no VS Code? (s/n) "
)

absolute_path = f"{current_directory}/{folder_name}"

if open_with_code == "s":
    system(f"code {current_directory}/{folder_name}")
else:
    match user_system:
        case "Windows":
                system(f"start {path.realpath(absolute_path)}")
        case "Linux":
                system(f"xdg-open {absolute_path}")
        case "Darwin": 
                system(f"open {absolute_path}")





