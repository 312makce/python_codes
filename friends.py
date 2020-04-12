user_input = input("Enter your friends name separated by , no space pls: ").split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(user_input)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nerby! Meet up with him')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
