def most_frequent():
   
    string = input("Enter a string: ")

    frequency = {}

    for char in string:
        
        if char in frequency:
            frequency[char] += 1
       
        else:
            frequency[char] = 1

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    for item in sorted_frequency:
        print(f"{item[0]}: {item[1]}")

most_frequent()
