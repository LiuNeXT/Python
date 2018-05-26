#!/usr/bin/env python
# -*- coding: utf-8 -*-

#程序绝对路径动态加载到环境变量
import os
import sys
#配置环境路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置程序路径
sys.path.append(BASE_DIR)
from conf import settings
from core import main

