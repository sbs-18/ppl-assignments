googledef webchecker(webs):
    if webs in ["google.com","facebook.com","netflix.com"]:
        print("Blocked")
    else:
        return
webchecker(input("Which website do you want to open?"))