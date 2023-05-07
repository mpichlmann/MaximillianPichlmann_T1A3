move = input("do you inspect the " + fg('yellow') + "[painting]" + attr('reset') + ", inspect the " + fg('yellow') + "[book]" + attr('reset') + " or head " + fg('yellow') + "[back]" + attr('reset') + "? ")


move = input("do you inspect the " + fg('yellow') + "[painting]" + attr('reset') + ", read the " + fg('yellow') + "[note]" + attr('reset') + " you found, or head " + fg('yellow') + "[back]" + attr('reset') + "? ")

move = input("do you inspect the " + fg('yellow') + "[book]" + attr('reset') + " or head " + fg('yellow') + "[back]" + attr('reset') + "? ")

move = input("do you inspect the " + fg('yellow') + "[box]" + attr('reset') + ", look at the " + fg('yellow') + "[photo]" + attr('reset') + ", or head " + fg('yellow') + "[back]" + attr('reset') + "? ")

move = input("do you look at the " + fg('yellow') + "[photo]" + attr('reset') + ", or head " + fg('yellow') + "[back]" + attr('reset') + "? ")

move = input("do you look at the " + fg('yellow') + "[photo]" + attr('reset') + " again, inspect the " + fg('yellow') + "[box]" + attr('reset') + ", or head " + fg('yellow') + "[back]" + attr('reset') + "? ")

print("maybe that " + fg('yellow') + "[note]" + attr('reset') + " you found earlier might help")

move = input("do you press one of symbols " + fg('yellow') + "[pig][bird][bear][baby][wheat][apple][sword][sheep][snake]" + attr('reset') + " \nor head " + fg('yellow') + "[back]" + attr('reset') + "? ")

move = input("do you " + fg('green') + "[rescue]" + attr('reset') + " the mechanic, or for some unimaginable reason head " + fg('yellow') + "[back]" + attr('reset') + " to the signpost? ")


print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("-------------------" + fg('red') + "YOU DIED: GAME OVER" + attr('reset') + "-------------------")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
print("------------------" + fg('green') + "YOU WIN: GAME COMPLETE" + attr('reset') + "---------------------")
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ")