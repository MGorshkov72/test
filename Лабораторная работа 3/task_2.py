def find_common_participants(people_1, people_2, n = ","):
    people = list(set(people_1.split(n)).intersection(people_2.split(n)))
    people.sort()
    return people

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,"|"))
