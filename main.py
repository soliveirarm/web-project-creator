from os import makedirs, getcwd, system

folder_name = input("Type in the name of your project's folder: ")

path = f"./{folder_name}"

try:
    makedirs(path)
    print("Folder created!\n")
except FileExistsError:
    folder_exists = input("This folder already exists! Do you wanna continue? (y/n) ")
    if folder_exists != "y":
        exit()

js_path = "app.js"
css_path = "style.css"

separate_js_folder = input(
    "Do you wanna create a 'js' folder for javascript files? (y/n) "
)

separate_css_folder = input("Do you wanna create a 'css' folder for css files? (y/n) ")

if separate_js_folder == "y":
    makedirs(f"{path}/js")
    js_path = "js/app.js"

if separate_css_folder == "y":
    makedirs(f"{path}/css")
    css_path = "css/style.css"

title = input("Type in the title of yor document (HTML's <title> tag): ")

with open(f"{path}/index.html", "w") as f:
    f.write(
        f"""<!DOCTYPE html>
<html lang="en">
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
    "\nYour project's been created! Would you like to open it with VS Code? (y/n) "
)

if open_with_code == "y":
    system(f"code {current_directory}/{folder_name}")
