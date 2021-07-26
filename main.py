import json
from pythonScripts import IMDbDatasets, DB_pgAdmin


class main:
    def __init__(self):
        with open('CONFIG.json') as config_file:
            self.data = json.load(config_file)

    def db_setup(self):
        """
        This function will setup the DB
        that will store all the data that is needed
        :return:
        """
        db_host, db_database, db_user, db_port, db_pass = \
            DB_pgAdmin.get_config_data(self.data)

        conn = DB_pgAdmin.connect_to_db(db_host, db_database,
                                        db_user, db_port, db_pass)

        DB_pgAdmin.create_tables(conn)

    def testStuff(self):
        db_host, db_database, db_user, db_port, db_pass = \
            DB_pgAdmin.get_config_data(self.data)

        conn = DB_pgAdmin.connect_to_db(db_host, db_database,
                                        db_user, db_port, db_pass)

        DB_pgAdmin.populate_tables(conn)

    def reset_imdb_datasets(self):
        """
        This function will re-download
        the data sets found on https://datasets.imdbws.com/
        """
        print('Download the IMDb datasets again')
        dataset_filenames = IMDbDatasets.get_ds_filenames(self.data)
        IMDbDatasets.download_ds_files(
            self.data['Dataset_IMDb_URL'],
            dataset_filenames
        )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    Start the main program
    """
    WhatsThatMovie = main()
    # WhatsThatMovie.reset_imdb_datasets()
    WhatsThatMovie.db_setup()
    WhatsThatMovie.testStuff()
