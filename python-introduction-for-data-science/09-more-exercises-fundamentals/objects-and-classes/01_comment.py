class Comment:
    def __init__(self, username, content, likes):
        self.username = username
        self.content = content
        self.likes = likes

#Test code
comment = Comment ("user1", "i like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

