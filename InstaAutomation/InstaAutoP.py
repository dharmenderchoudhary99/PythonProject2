from instabot import Bot
from instabot.bot.bot_follow import follow

bot=Bot()
bot.login(username="Yourusername",password="Yourpassword")

#follow the id you entered
# bot.follow('Followerid')

#upload the pic
# bot.upload_photo("PhotoPath",caption="I love python")

#Unfollow the id you mentioned
# bot.unfollow('unfollower username')

#Send message to one or more user id
# bot.send_message("Hi i am new",["User id2","user id2"])

#get the info of your followers
# followers = bot.get_user_followers("yourusername")
# for follower in followers:
#     print(bot.get_user_info(follower))

#Get name of following
following=bot.get_user_following("uyourusername")
for following in following:
    print(bot.get_user_info(following))