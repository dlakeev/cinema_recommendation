from tqdm import tqdm
import pandas as pd
from sqlalchemy import create_engine
from configs.server_config import ENGINE_LINK


def load_data(table_name: str, type: str, kp_num: int, output_path: str = './data/data') -> None:
    q = f'''
    select
        *
    from
        {table_name}
    where
        type = '{type}'
        and description notnull
        and kp_num::int >= {kp_num}
    '''

    with create_engine(ENGINE_LINK).connect() as conn:
        pd.read_sql(q, conn).to_csv(f'{output_path}.csv', index=False)


def load_data_description(table_name: str, output_path: str = './data/data_description') -> None:
    q = f'''
    select
        cols.column_name,
        (
            select
                pg_catalog.col_description(c.oid, cols.ordinal_position::int)
            from pg_catalog.pg_class c
            where
                c.oid = (select cols.table_name::regclass::oid) and c.relname = cols.table_name
        ) as description
    from
        information_schema.columns cols
    where
        cols.table_schema  = 'public' and
        cols.table_name = '{table_name}';
    '''

    with create_engine(ENGINE_LINK).connect() as conn:
        pd.read_sql(q, conn).to_csv(f'{output_path}.csv', index=False)


if __name__ == '__main__':
    load_data(table_name='tvs', type='Фильм', kp_num=5000)
    load_data_description(table_name='tvs')
