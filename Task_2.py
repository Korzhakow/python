def my_func(name, surname, year, city, email, telephone):
    return " ".join([name, surname, year, city, email, telephone])


print(my_func(surname="Bondarev", name="Vladimir", year="1993", city="Volgograd", email="qwerty@mail.ru",
              telephone="8-800-555-35-55"))
