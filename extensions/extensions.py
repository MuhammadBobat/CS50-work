file = input("File Name:").lower().strip()
if ".gif" in file:
    print("image/gif")
elif ".jpeg" in file:
    print("image/jpeg")
elif ".jpg" in file:
    print("image/jpeg")
elif file.endswith(".png") == True:
    print("image/png")
elif file.endswith(".pdf") == True:
    print("application/pdf")
elif file.endswith(".txt") == True:
    print("text/plain")
elif file.endswith(".zip") == True:
    print("application/zip")
else:
    print("application/octet-stream")