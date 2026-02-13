#Read user input
start=ord(input())
end=ord(input())

# Logic
def characters(s:int, e:int)-> str:
    output = ""
    for i in range(s+1, e):
        output += chr(i) + " "
    return output
result = characters(s=start, e=end)

# Print output
print(result)