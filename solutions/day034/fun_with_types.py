# fun with data types
# age: int
name: str
height: float
is_human: bool


def police_check(
    age: int,
) -> (
    bool
):  # we can specify the type of the argument inputs (int here), as well as the return type of the function (bool here)
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(16))
print(police_check(19))

if police_check(16):
    print("You can drive")
else:
    print("You can't drive")
