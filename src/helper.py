import faker


def get_sign_up_data() -> tuple[str, str]:
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password
