#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:23:42 2020

@author: kejin
"""

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import Bio
from Bio import SeqIO
from Bio import Seq

driver=webdriver.Chrome('/Users/kejin/local/bin/chromedriver')
batch=input("Enter the batch no.: ")

sequence_with_result=[]
with open("sequences{0}.fasta".format(batch),"rU") as handle, open("sequence_with_result{0}.fasta".format(batch),"w") as handle2:
    for record in SeqIO.parse(handle,"fasta"):
        sequence=record.seq
        
        driver.get("http://genesilico.pl/rrm/find/")
        sequence_field=driver.find_element_by_id('id_sequence_field')
        sequence_field.click()
        sequence_field.send_keys(sequence)

        submit_btn=driver.find_element_by_name('submit')
        submit_btn.click()

        timeout=30
        
        try: 
            header_presence=EC.presence_of_element_located((By.TAG_NAME,'h1'))
            WebDriverWait(driver, timeout).until(header_presence)
            header_location=driver.find_element_by_tag_name("h1")
            if header_location.text=="No result":
                pass
            else:
                sequence_with_result.append(record)
                print("Has result: "+record.id)
                SeqIO.write(record,handle2,'fasta')
    
        except TimeoutException:
            print("Time out waiting for page to load: "+record.id)
            pass
            


