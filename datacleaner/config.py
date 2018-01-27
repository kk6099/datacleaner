# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------------------------------------------#
# author: sean lee                           #
# email: lxm_0828@163.com                    #
#--------------------------------------------#

"""MIT License

Copyright (c) 2018 Sean

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import os

app_root = os.sep.join(__file__.split(os.sep)[:-1])
stopwords_path = os.path.join(app_root, os.path.join('data', 'stopwords.txt'))
drawer_bg = os.path.join(app_root, os.path.join('data', 'cloud_background.png'))
drawer_font = os.path.join(app_root, os.path.join('data', 'font.ttf'))