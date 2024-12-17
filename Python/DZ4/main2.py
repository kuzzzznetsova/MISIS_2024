file = 'Моя диссертац.gif'
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

def check_extension(file_name):
    file_extension = file_name.split('.')[-1] #извлечение расширения файла из имени файла
    if file_extension.lower() in extensions:
        print(f"The file {file_name} has a valid extension.")
    else:
        print(f"The file {file_name} has an invalid extension.")

check_extension(file)
