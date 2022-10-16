
def test():
    print("Help im a function")

test()

year = 52
day_list = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

for ii in range(year):
    for i in day_list:
        text = f"happy {i}"
        real_thoughts = "Life goes around in circles."
        print (text)
        if "day" in text:
            print(real_thoughts)
