Python 3.x is required

#### required package:
1. reportlab
2. PyPDF2

```
pip3 install reportlab
pip3 install PyPDF2
```

#### usage
make sure the PFD file (__input.pdf__) ready to be watermarked is in the same folder, 
```
python pdf_watermark_embed.py input.pdf tmp.pdf "TEST" out.pdf
python pdf_watermark_embed.py [path of input file (file needed)] [path of intermediate file] [text that you want to use as the watermark] [path of the output file]
```
