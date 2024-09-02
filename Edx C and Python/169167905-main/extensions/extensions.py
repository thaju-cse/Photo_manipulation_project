temp = (input("File name: ").lower()).strip()
if (temp[-3:] == "jpg"):
    print("image/jpeg")
elif (temp[-3:] == "pdf"):
    print("application/pdf")
elif (temp[-3:] == "gif"):
    print("image/gif")
elif (temp[-3:] == "png"):
    print("image/png")
elif (temp[-3:] == "txt"):
    print("text/plain")
elif (temp[-3:] == "zip"):
    print("application/zip")
elif (temp[-4:] == "jpeg"):
    print("image/jpeg")
else:
    print("application/octet-stream")
