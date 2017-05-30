'''
    File name: main.py
    Author: Daniela Pralon, João Paulo Reis Alvarenga, Manoel Stilpen, Marina Lima, Patrick Rosa
    Date created: 5/30/2017
    Data last modified: 5/30/2017
    Python version: 2.7
    License: GPL
'''

from camadafisica import CamadaFisica
from camadaenlace import CamadaEnlace


camada_fisica = CamadaFisica('TCP', '127.0.0.1', '666')
camada_enlance = CamadaEnlace(0.1, 0.01, 0.01)