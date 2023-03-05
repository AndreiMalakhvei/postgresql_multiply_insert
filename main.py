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

    database.table_create()
    obj_lst_one = create_obj_list(1000)
    obj_list_ten = create_obj_list(10000)
    tup_list_one = create_tuple_list(1000)
    tup_list_ten = create_tuple_list(10000)

    print('Inserting objects one by one')
    insert_one_by_one(obj_lst_one)

    print('*'*70 + '\n' + 'Inserting tuples one by one')
    insert_one_by_one(obj_lst_one)


    print('*'*70 + '\n' + 'Inserting tuples with batch')
    batch_insert(tup_list_one)

    print('*' * 70 + '\n' + 'Inserting tuples with values')
    values_insert(obj_lst_one)
