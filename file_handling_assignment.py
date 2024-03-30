with open("my_file.txt",'a+') as file:
    try:
      file.writelines("A student,\nIndex 345,\nPower  Learn Academy")
      file.writelines("\nSpecializing python,\nInterested in web development")
      file.seek(0)
      data = file.readlines()
      print(data)
    except FileNotFoundError:
      print("File not found.")
    except PermissionError:
      print("Permission denied.")
    finally:
       file.close()
