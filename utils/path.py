# -*- coding: utf-8 -*-
import os

project_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def pathjoin(*args):
    return os.path.join(project_dir, *args)