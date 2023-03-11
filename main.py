from dbs.db_create import PostgresqlDB
from timer import timer
from objs import create_obj_list, create_tuple_list
from tqdm import tqdm

database = PostgresqlDB()


@timer
def insert_one_by_one(lst):
    for rec in tqdm(lst, desc='SAVING RECORDS'):
        database.save_single_record(rec)


@timer
def batch_insert(lst):
    database.save_batch(lst)


@timer
def values_insert(obs_list):
    database.save_values(obs_list)


if __name__ == "__main__":

    number_of_records = 1000

    database.table_create()
    obj_lst = create_obj_list(number_of_records)
    tup_list = create_tuple_list(number_of_records)


    print('Inserting objects one by one')
    one_by_one_time = insert_one_by_one(obj_lst)

    print('*'*70 + '\n' + 'Inserting tuples with batch')
    batch_time = batch_insert(tup_list)
    print(f'batch is {one_by_one_time / batch_time } times faster')


    print('*' * 70 + '\n' + 'Inserting tuples with values')
    values_time = values_insert(obj_lst)
    print(f'values insert is {one_by_one_time / values_time} times faster')

    database.delete_all()
