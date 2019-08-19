import pytest

from utils.central import CentralUtils


class TestDataSource(object):

    @pytest.mark.sanity
    def test_add_database(self, selenium):
        """
        TestCase Title:
            Add Database
        """
        self.generic_utils = CentralUtils(driver=selenium)
        self.generic_utils.launch_and_login("usr01", "usr01@123")
        self.generic_utils.add_database(database_name="hive_harshit", sql_alchemy_uri="hive://rafint001-slv-01.cloud.in.guavus.com:10000/", extras='''{
"metadata_params": {},
"engine_params": {
"connect_args": {
"kerberos_service_name":"hive",
"auth": "KERBEROS"
}
},
"metadata_cache_timeout": {},
"schemas_allowed_for_csv_upload": []
}''')

    @pytest.mark.sanity
    def test_add_table(self, selenium):
        """
        TestCase Title:
            Add Database Table
        """
        self.generic_utils = CentralUtils(driver=selenium)
        self.generic_utils.launch_and_login("usr01", "usr01@123")
        self.generic_utils.add_table(database_name="hive_harshit", schema_name="hive_test", table_name="vzw_raw_agg")

    @pytest.mark.sanity
    def test_create_table_slice(self, selenium):
        """
        TestCase Title:
            Create a basic Table Slice
        """
        self.generic_utils = CentralUtils(driver=selenium)
        self.generic_utils.launch_and_login("usr01", "usr01@123")
        self.generic_utils.create_new_chart(data_source_name="hive_test.vzw_raw_agg", chart_name="test_Chart12", column_name="imsi", row_limit="11")
