#!/usr/bin/env python

import pickle

penn_to_lets_dict = {}
penn_to_lets_dict['CC'] = 'VG'
penn_to_lets_dict['CD'] = 'TW'
penn_to_lets_dict['DT'] = 'LID'
penn_to_lets_dict['EX'] = 'SPEC'
penn_to_lets_dict['FW'] = 'SPEC'
penn_to_lets_dict['IN'] = 'VZ'
penn_to_lets_dict['JJ'] = 'ADJ'
penn_to_lets_dict['JJR'] = 'ADJ'
penn_to_lets_dict['JJS'] = 'ADJ'
penn_to_lets_dict['LS'] = 'SPEC'
penn_to_lets_dict['MD'] = 'SPEC'
penn_to_lets_dict['NN'] = 'N'
penn_to_lets_dict['NNS'] = 'N'
penn_to_lets_dict['NNP'] = 'N'
penn_to_lets_dict['NNPS'] = 'N'
penn_to_lets_dict['PDT'] = 'LID'
penn_to_lets_dict['POS'] = 'SPEC'
penn_to_lets_dict['PRP'] = 'VNW'
penn_to_lets_dict['PRP$'] = 'VNW'
penn_to_lets_dict['RB'] = 'BW'
penn_to_lets_dict['RBR'] = 'BW'
penn_to_lets_dict['RBS'] = 'BW'
penn_to_lets_dict['RP'] = 'SPEC'
penn_to_lets_dict['SYM'] = 'SPEC'
penn_to_lets_dict['TO'] = 'SPEC'
penn_to_lets_dict['UH'] = 'TSW'
penn_to_lets_dict['VB'] = 'WW'
penn_to_lets_dict['VBD'] = 'WW'
penn_to_lets_dict['VBG'] = 'WW'
penn_to_lets_dict['VBN'] = 'WW'
penn_to_lets_dict['VBP'] = 'WW'
penn_to_lets_dict['VBZ'] = 'WW'
penn_to_lets_dict['WDT'] = 'LID'
penn_to_lets_dict['WP'] = 'VNW'
penn_to_lets_dict['WP$'] = 'VNW'
penn_to_lets_dict['WRB'] = 'BW'


pkl_file = open('./penn_to_lets.pkl', 'wb')
pickle.dump(penn_to_lets_dict, pkl_file)
pkl_file.close()


