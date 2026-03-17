followers = {}

while True:
    command_input = input()

    if command_input == "Log out":
        break

    commands = command_input.split(": ")
    cmd = commands[0]

    if cmd == "New follower":
        username = commands[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif cmd == "Like":
        username = commands[1]
        count = int(commands[2])

        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count

    elif cmd == "Comment":
        username = commands[1]

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif cmd == "Blocked":
        username = commands[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

# Print output
print(f"{len(followers)} followers")
for username, data in followers.items():
    total = data["likes"] + data["comments"]
    print(f"{username}: {total}")

# followers = {}
# likes_count = 0
# comments_count = 0
# sum_likes_comments = 0
# followers_count = 0
# while True:
#     commands = input().split(": ")
#     if commands == "Log out":
#         break
#
#     username = commands[1]
#
#
#     if commands[0] == "New follower":
#         if username not in followers:
#             followers[username] = likes_count
#             comments_count = 0
#             followers[username] = comments_count
#             followers_count += 1
#         else:
#             continue
#
#     if commands[0] == "Like":
#         if username not in followers:
#             count = int(commands[2])
#             sum_likes_comments = count + comments_count
#             followers[username] = sum_likes_comments
#         else:
#             count = int(commands[2])
#             likes_count += count
#             followers[username] += likes_count
#     if commands[0] == "Comment":
#         if username not in followers:
#             comments_count = 1
#             followers[username] = comments_count
#         else:
#             comments_count += 1
#             followers[username] += comments_count
#     if commands[0] == "Blocked":
#         followers.pop(username)
#
# #Extract data, Print output
# print(f"{followers_count} followers")
# for username, likes_comments in followers.items():
#     print(f"{username}: {likes_comments}")


'''
In the end, you have to print the count of followers, each follower with their likes and comments (the sum of likes and comments):
"{count} followers"
{username}: {likes+comments}
{username}: {likes+comments}
…
{username}: {likes+comments}"




'''

'''

Последователи
Създайте програма, която съхранява информацията за последователите на Джейн във Facebook, техните харесвания и коментари.
Записвайте последователите, всеки с броя на харесванията и коментарите, които Джейн е получила от тях.
Ще получавате редове с команди, докато не получите командата „Изход“. Има четири възможни команди:
• „Нов последовател: {username}“:
o Добавете потребителското име към вашите записи (с 0 харесвания и 0 коментара).
o Ако вече съществува човек с даденото потребителско име, игнорирайте реда.
• „Харесване: {username}: {count}“:
o Ако потребителското име не съществува, добавете го към вашите записи с дадения брой харесвания.
o Ако потребителското име съществува, увеличете броя на харесванията с дадения брой.
• „Коментар: {username}“:
o Ако потребителското име не съществува, добавете го към вашите записи с 1 коментар.
o Ако потребителското име съществува, увеличете броя на коментарите с 1.
• "Блокирано: {потребителско име}":
o Изтрийте всички записи за даденото потребителско име.
o Ако не съществува, изпишете: "{потребителско име} не съществува."

Накрая трябва да изпишете броя на последователите, всеки последовател с неговите харесвания и коментари (сумата от харесванията и коментарите):


'''


'''
Followers
Create a program that keeps the information about Jane's Facebook followers, their likes, and comments. 
Keep a record of the followers, each with the count of likes and comments Jane has received from them.
You will be receiving lines with commands until you receive the "Log out" command. There are four possible commands:
•	"New follower: {username}":
o	Add the username to your records (with 0 likes and 0 comments).
o	If a person with the given username already exists, ignore the line.
•	"Like: {username}: {count}":
o	If the username doesn't exist, add it to your records with the given count of likes.
o	If the username exists, increase the count of likes with the given count.
•	"Comment: {username}":
o	If the username doesn't exist, add it to your records with 1 comment.
o	If the username exists, increase the count of comments with 1.
•	"Blocked: {username}":
o	Delete all records of the given username. 
o	If it doesn't exist, print: "{Username} doesn't exist."
In the end, you have to print the count of followers, each follower with their likes and comments (the sum of likes and comments):
"{count} followers"
{username}: {likes+comments}
{username}: {likes+comments}
…
{username}: {likes+comments}"
Input
•	You will be receiving lines until you receive the "Log out" command.
•	The input will always be valid.
Output
•	Print the users with their likes in the format described above.


Examples
Input	Output
New follower: George
Like: George: 5
New follower: George
Log out	1 followers
George: 5

Like: Katy: 3
Comment: Katy
New follower: Bob
Blocked: Bob
New follower: Amy
Like: Amy: 4
Log out	2 followers
Katy: 4
Amy: 4
Blocked: Amy
Comment: Amy
New follower: Amy
Like: Tom: 5
Like: Ellie: 5
Log out	Amy doesn't exist.
3 followers
Amy: 1
Tom: 5
Ellie: 5

'''


