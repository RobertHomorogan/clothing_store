import datetime
from sqlalchemy import create_engine, text

from Domain.client import Client

engine = create_engine('mysql+pymysql://root:@localhost:3306/store', echo=False)


CATEGORY_LIST = ['tops', 'pants', 't-shirts', 'jackets', 'sneakers', 'baby']


def read_float(input_text, retries=10):
    """
    Tries for 'retries' times to read a float, and return it.
    If it cannot read it in 'reties' times it raises ValuesError
    :param input_text: string
    :param retries: int (default 10)
    :return: String converted to float if possible
    :raises: ValueError if no float is given in maximum 'retries' times
    """
    times_retied = 0
    while times_retied < retries:
        read_value = input(input_text)
        if validate_float(value=read_value):
            return float(read_value)

        print('This value is not a float')
        times_retied += 1

    print('You are not that bright!')
    raise ValueError


def validate_float(value):
    """
    This function validates that a string can be converted into a float
    :param value: string
    :return: True if it can be transformed into a float, False otherwise
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_age_group(cnp):
    today = datetime.datetime.today()

    if int(cnp[0]) <= 2:
        decades = 1900
    else:
        decades = 2000
    born = datetime.datetime(
        year=int(cnp[1:3]) + decades,
        month=int(cnp[3:5]),
        day=int(cnp[5:7]))
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if age < 18:
        return '<18'
    if 18 <= age <= 24:
        return '18-24'
    if 25 <= age <= 34:
        return '25-34'
    if 35 <= age <= 44:
        return '35-44'
    if 45 <= age <= 54:
        return '45-54'
    if age >= 55:
        return '>=55'


if __name__ == '__main__':
    all_clients = []
    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM clients'))
        for item in query:
            client = Client(
                cnp=item[0],
                first_name=item[1],
                last_name=item[2],
                email=item[3],
            )
            all_clients.append(client)
    print(all_clients)
    with engine.connect() as conn:
        query = conn.execute(text('SELECT * FROM products'))
        for item in query:
            print(item)
        product_id = 1
        conn.execute(text(f'DELETE FROM products WHERE product_id = {product_id}'))
