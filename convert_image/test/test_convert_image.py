#
# @test_convert_image.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information").  You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from pathlib import Path
from unittest import TestCase
from wand.image import Image

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class TestImageConverter(TestCase):
    """Class to test functions of the library to convert images, using some effects or dimensions changes"""

    def test_convert_grayscale(self):
        filepath = str(BASE_DIR) + '/resources_test/google.jpg'
        with Image(filename=filepath) as img:
            img.type = 'grayscale'
            self.assertTrue(img)

    def test_convert_resize(self):
        filepath = str(BASE_DIR) + '/resources_test/google.jpg'
        with Image(filename=filepath) as img:
            width = 1000
            height = 500
            img.resize(width, height)
            current = str(img.size)

            expected = "(1000, 500)"
            self.assertEqual(current, expected)
