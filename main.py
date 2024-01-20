from os import makedirs, getcwd, startfile, system


for _ in range(29):
    print("\n")

folder_name = input("Nome da pasta do seu projeto: ")

try:
    makedirs(f"./{folder_name}")
    print("Pasta criada!\n")
except FileExistsError:
    folder_exists = input("Essa pasta já existe! Deseja continuar? (s/n) ")
    if folder_exists != "s":
        exit()


path = f"./{folder_name}"

title = input("Digite o título do seu documento(<title> do seu HTML): ")

with open(f"{path}/index.html", "w") as f:
    f.write(
        f"""<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <script src="script.js"></script>
  </body>
</html>
"""
    )

with open(f"{path}/style.css", "w") as f:
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


open(f"{path}/script.js", "w")

current_directory = getcwd()

open_with_code = input(
    "\nTudo pronto! Você gostaria de abrir a pasta no VS Code? (s/n) "
)

if open_with_code == "s":
    system(f"code {current_directory}/{folder_name}")
else:
    startfile(f"{current_directory}/{folder_name}")
