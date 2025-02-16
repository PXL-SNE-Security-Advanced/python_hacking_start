def function():
    y = "local"  # Local scope
    print("Inside function:", y)

function()
# print(y)  # This would raise an error because y is not accessible here.