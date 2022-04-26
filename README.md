# Segment Dummy Data generator
A litlle tool for genrating dummy segment data for testing purposes.
For running just :
```bash
python3 -m segment_data_generator.run  --key SEGMENT_WRITE_KEY       
```
Cli Usage
```
usage: run.py [-h] [--version] [-v] [-vv] -k WRITE_KEY

Segment Data generator

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set loglevel to INFO
  -vv, --very-verbose   set loglevel to DEBUG
  -k WRITE_KEY, --key WRITE_KEY
                        put your segment write key


```