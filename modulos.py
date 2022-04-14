from __future__ import print_function
from argparse import FileType
from cProfile import label

import os
import os.path
import pathlib
from statistics import mode
import tkinter.ttk as ttk
from tkinter import *
import PyPDF2
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog


import pygubu
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from setuptools import Command