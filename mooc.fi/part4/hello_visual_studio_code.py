while True:
    editor = input("Editor: ")
    print(editor)

    if editor == "word" or editor == "notepad":
        print("awful")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
