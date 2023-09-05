# 98
class User:
    id = 1

u = User()
# u.id = 2
User.id = 98
print(u.id)


# 89
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)

# 98
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)