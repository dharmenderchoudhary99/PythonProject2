from skpy import Skype

slogin = Skype("Email ID","Password")

ch=slogin.contacts["id"]
with open("Image path","rb") as f:
    ch.chat.sendFile(f,"imagefilename",image=True)


# # for group
# group=slogin.chats.create(["other account holder id1","id2","id3"])


# # For a contact sending message
# contact= slogin.contacts["Id of person"]
# contact.chat.sendMsg("Welcome to my world")

# for i in contact:
#     print(i)