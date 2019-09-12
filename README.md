# AWS textract

Supporting Code for Blog at https://www.linkedin.com/pulse/how-i-scanned-translated-document-using-aws-textract-anshumali-sharma/

The chosen document Below.JPG is uploaded to the bucket and then scanned using AWS textract to obtain the text in it.

Result is values from the scanned document in plain text:

```
~/workspace/textract $ python3 scanform.py
Key Value Pairs:
Detected Key: Legal Guardian:, Detected Value: NOT_SELECTED
Detected Key: Date of Issue of Nationality Document, Detected Value: None
Detected Key: Residence (country), Detected Value: Belize
Detected Key: Colour of hair, Detected Value: Black
Detected Key: Father:, Detected Value: NOT_SELECTED
Detected Key: (A) The information given here is correct to the best of my knowledge and belief;, Detected Value: NOT_SELECTED
Detected Key: Dote of Birth (doy/month/ye, Detected Value: 1/08/2005
Detected Key: Divorced, Detected Value: NOT_SELECTED
Detected Key: Colour of eyes, Detected Value: Brown
Detected Key: Applicants's Notionality, Detected Value: Belizean
Detected Key: Occupotion, Detected Value: Student
```
