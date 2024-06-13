
#Task 1
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2
text = input("How are you feeling? Happy? Sad? - You:")
output = ""

if "happy" in text:
    output = "That's great to hear!"
elif "sad" in text:
    output = "I hope your day gets better!"
else:
    output = "Interesting, see ya later!"

print(output)
