def create_fdb(fdb):
    '''
        Item 1: 15%

        GIVEN: expected_fdb_schema
        user_fdb_schema = extract fdb schema
        comapre user_fdb_schema and expected_fdb_schema
    '''
    pass


def extract_files(files_path):
    '''
        Item 2: 10%

        GIVEN: expected list of raw files
        check if expected list of files are in the directory files_path
    '''
    pass


def transform_files(slc):
    '''
        Item 3: 15%

        GIVEN: expected_transformed_files
        run ngen using slc
        compare the generated files to the expected files
    '''
    pass


def load(fdb):
    '''
        Item 4: 10%

        GIVEN: expected fdb
        diff fdb and expected fdb
    '''
    pass


def create_worflow(username):
    '''
        Item 5: 25%

        GIVEN:
            - workflow name: username_content_lab
            - quetex       : username_test
            - DBL          : CIE_MANILA_TRAIN_DBL
            - schedule     : Mon - Fri, 6PM ET
        get workflow
        assert workflow name
        assert quetex used
        assert DBL used
        assert schedule
    '''
    pass


def run_worflow():
    '''
        Item 6: 5%

        GIVEN: expected dates
        get worflow runs
        get dates
        assert dates and expected dates
    '''
    pass


def fdb_add_field_shares(fdb):
    '''
        Item 7: 5%

        check if shares field exists in fdb
    '''
    pass


def fdb_add_field_mcap(fdb):
    '''
        Item 8: 5%

        check if mcap field exists in fdb
    '''
    pass


def fdb_shares_mcap_data_check(fdb):
    '''
        Item 9: 10%

        GIVEN: expected fdb
        diff fdb and expected fdb
    '''
    pass


def is_equal(arg1, arg2):
    try:
        assert arg1 == arg2
        return True
    except AssertionError:
        return False
