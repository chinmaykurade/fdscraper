# -*- coding: utf-8 -*-
from . import gss,download,gtc


def fscore(file_path,driver_path,out_path,data=None,ol=None):
    all_data=download.from_file(file_path,driver_path,out_path)

    ss,ol=gss.get_similar_sectors(out_path,5)
    
    cols = ['Company_name','DE','PE','ROE','Market Cap','Revenue Growth','PAT Growth','Score(10)']
    
    results = gtc(ol[0])[cols]
    
    return results