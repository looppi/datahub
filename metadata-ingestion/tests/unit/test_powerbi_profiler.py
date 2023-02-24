from datahub.ingestion.source.powerbi.rest_api_wrapper.powerbi_profiler import (
    process_sample_result,
)

result = {
    "results": [
        {
            "tables": [
                {
                    "rows": [
                        {
                            "TEST_TBL[SEQ]": None,
                            "TEST_TBL[LVL1_NR]": "1",
                            "TEST_TBL[LVL3_NAME]": "FINLAND",
                            "TEST_TBL[NUMBER]": "25499",
                            "TEST_TBL[SOURCE]": "SERVICE",
                            "TEST_TBL[VALID_FROM]": "2018-08-23T02:45:09",
                            "TEST_TBL[VALID_TO]": "9999-12-31T00:00:00",
                            "TEST_TBL[COMPANY_ID]": "6",
                        },
                        {
                            "TEST_TBL[SEQ]": None,
                            "TEST_TBL[LVL1_NR]": "1",
                            "TEST_TBL[LVL3_NAME]": "FINLAND",
                            "TEST_TBL[NUMBER]": "12244",
                            "TEST_TBL[SOURCE]": "SERVICE",
                            "TEST_TBL[VALID_FROM]": "2000-01-01T00:00:00",
                            "TEST_TBL[VALID_TO]": "9999-12-31T00:00:00",
                            "TEST_TBL[COMPANY_ID]": "5",
                        },
                    ]
                }
            ]
        }
    ]
}


def test_sample_result_parsing():
    processed = process_sample_result(result)
    assert 7 == len(processed)
    assert 2 == len(processed["VALID_FROM"])
