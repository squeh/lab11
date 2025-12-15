for bull in range(1,11):
    for cow in range(1,21):
        for telenok in range(1,201):
            if bull * 10 + cow * 5 + telenok * .5 == 100:
                print(f"""
Быков: {bull},
Коров: {cow},
Телят: {telenok}
""")
