import unittest
from locations import TestAOL


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestAOL('add_location_successfully'))
    suite.addTest(TestAOL('add_location_failed_blank_all_fields'))
    suite.addTest(TestAOL('add_location_failed_blank_name_fields'))
    suite.addTest(TestAOL('add_location_successfully_blank_city_fields'))
    suite.addTest(TestAOL('add_location_successfully_blank_state_fields'))
    suite.addTest(TestAOL('add_location_successfully_blank_pcode_fields'))
    suite.addTest(TestAOL('add_location_failed_blank_country_fields'))
    suite.addTest(TestAOL('add_location_successfully_blank_phone_fields'))
    suite.addTest(TestAOL('add_location_failed_due_to_invalid_phone'))
    suite.addTest(TestAOL('add_location_successfully_blank_fax_fields'))
    suite.addTest(TestAOL('add_location_failed_due_to_invalid_fax'))
    suite.addTest(TestAOL('add_location_successfully_blank_address_fields'))
    suite.addTest(TestAOL('add_location_successfully_blank_notes_fields'))
    suite.addTest(TestAOL('cancel_add_location'))
    suite.addTest(TestAOL('search_location_successfully_by_name'))
    suite.addTest(TestAOL('search_location_failed_due_to_invalid_name'))
    suite.addTest(TestAOL('search_location_failed_due_to_invalid_city'))
    suite.addTest(TestAOL('edit_location_successfully'))
    suite.addTest(TestAOL('cancel_edit_location'))
    suite.addTest(TestAOL('delete_location_successfully'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
