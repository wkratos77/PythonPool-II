def ft_count_harvest_recursive(day=1):
    if (day == 1):
        ft_count_harvest_recursive.days = int(input("Days until harvest: "))
    if day > ft_count_harvest_recursive.days:
        print("Harvest time!")
        return
    print("Day", day)
    ft_count_harvest_recursive(day + 1)
