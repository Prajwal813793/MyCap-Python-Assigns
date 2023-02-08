filename = input("Input the Filename: ")
extension = filename.rsplit(".", 1)[-1]

if extension == "py":
    extension = "python"

print("The extension of the file is : '{}'".format(extension))
