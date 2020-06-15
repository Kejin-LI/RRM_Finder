RRM Finder
RNA recognition motif, RRM is a conserved protein domain of about 90 amino acids that often binds single-stranded RNAs and may have other roles such as protein- or DNA binding. This program is therefore designed to find rrms(RNA Recognition Motifs) of multiple protein sequences from the RNA Recognition Motif Database online(http://genesilico.pl/rrm/).

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
What things you need to install the software and how to install them:
1. Python3
2. Site-packages installed in Python3: 
   1) selenium: If you haven pip on your system, you can simply install or upgrade the Python bindings: pip install -U selenium. You can obtain more information from the website: https://pypi.org/project/selenium/.
   2) drivers: Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin. Other supported browser browser can also be used, such as Chrome, Safari and Edge. You can obtain more information from the website: https://pypi.org/project/selenium/.
   3) Biopython: Try: pip install biopython. For updating an older version of Biopython try: pip install biopython --upgrade. You can obtain more information from the website: https://biopython.org/wiki/Download.
   
Running the tests
Explain how to run the automated tests for this system:
1. Open your terminal or Linux/Unix system and type:
python3 rrm_finder.py
2. Name your protein sequences file as: sequences1.fasta, sequences2.fasta, or sequences3.fasta. In this packages, you are given a test protein fasta file named "sequences1.fasta", you can use this file to test the python3 script.
3. After running the python3 script, you should type the batch No. on your system. The batch No. refers to the number of your input fasta file. For example, if your input protein fasta file is named "sequences1.fasta", you should type "1". Then the progress wil start.