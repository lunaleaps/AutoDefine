import unittest
from json_api import get_definitions

TEST_DEF = {"def": [
            {
                "sseq": [
                    [
                        [
                            "sense",
                            {
                                "sn": "1",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}the degree of loudness or the intensity of a sound"
                                    ]
                                ],
                                "sdsense": {
                                    "sd": "also",
                                    "dt": [
                                        [
                                            "text",
                                            "{bc}{sx|loudness||}"
                                        ]
                                    ]
                                }
                            }
                        ]
                    ],
                    [
                        [
                            "sense",
                            {
                                "sn": "2",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}the amount of space occupied by a three-dimensional object as measured in cubic units (such as quarts or liters) {bc}cubic capacity {dx}see {dxt|Metric System Table|metric system|table}, {dxt|Weights and Measures Table|weight|table}{/dx}"
                                    ]
                                ]
                            }
                        ]
                    ],
                    [
                        [
                            "pseq",
                            [
                                [
                                    "sense",
                                    {
                                        "sn": "3 a (1)",
                                        "dt": [
                                            [
                                                "text",
                                                "{bc}{sx|amount||}"
                                            ]
                                        ],
                                        "sdsense": {
                                            "sd": "also",
                                            "dt": [
                                                [
                                                    "text",
                                                    "{bc}{sx|bulk||}, {sx|mass||}"
                                                ]
                                            ]
                                        }
                                    }
                                ],
                                [
                                    "sense",
                                    {
                                        "sn": "(2)",
                                        "dt": [
                                            [
                                                "text",
                                                "{bc}a considerable quantity"
                                            ]
                                        ]
                                    }
                                ]
                            ]
                        ],
                        [
                            "sense",
                            {
                                "sn": "b",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}the amount of a substance occupying a particular volume"
                                    ]
                                ]
                            }
                        ],
                        [
                            "sense",
                            {
                                "sn": "c",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}mass or the representation of mass in art or architecture"
                                    ]
                                ]
                            }
                        ]
                    ],
                    [
                        [
                            "sense",
                            {
                                "sn": "4 a",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}a series of printed sheets bound typically in book form {bc}{sx|book||}"
                                    ]
                                ]
                            }
                        ],
                        [
                            "sense",
                            {
                                "sn": "b",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}a series of issues of a periodical"
                                    ]
                                ]
                            }
                        ],
                        [
                            "sense",
                            {
                                "sn": "c",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}{sx|album||1c}"
                                    ]
                                ]
                            }
                        ]
                    ],
                    [
                        [
                            "sense",
                            {
                                "sn": "5",
                                "dt": [
                                    [
                                        "text",
                                        "{bc}{sx|scroll||1a}"
                                    ]
                                ]
                            }
                        ]
                    ]
                ]
            }
            ]}


class TestJsonAPI(unittest.TestCase):

    def test_get_definitions(self):
        dts = get_definitions(TEST_DEF)
        print(len(list(dts)))
        # for dt in dts:
        #     print(dt)


if __name__ == '__main__':
    unittest.main()
