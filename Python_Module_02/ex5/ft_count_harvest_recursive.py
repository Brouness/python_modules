def ft_print_days(x, a) -> None:
    print("Day", a)
    if a < x:
        ft_print_days(x, a + 1)


def ft_count_harvest_recursive() -> None:
    a = int(input("Days until harvest: "))
    x = 1
    if a > 0:
        ft_print_days(a, x)
    print("Harvest time!")
