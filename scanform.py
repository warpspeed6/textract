import boto3

# Get the helper function so we can parse the textract response
# https://github.com/aws-samples/amazon-textract-response-parser
from trp import Document

'''Get the helper function so we can parse the textract response'''

#  What are we scanning
Bucket = "anshu-textract-rax"
doco_for_scan = "Below.jpg"

# Setup Boto3 client
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html

textract = boto3.client('textract', region_name="us-east-1")

response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': Bucket,
            'Name': doco_for_scan
        }
    },
    FeatureTypes=["FORMS"])
    # 'TABLES'|'FORMS'

extract = Document(response)

# Start looping
for page in extract.pages:
    print("Key Value Pairs:")
    for headings in page.form.fields:
        print("Detected Key: {}, Detected Value: {}".format(headings.key, headings.value))

# Amazon Translate client
translate = boto3.client('translate')

# Use the same response to translate

print ('Lets Translate using AWS translate')
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print (item["Text"])
        result = translate.translate_text(Text=item["Text"], SourceLanguageCode="en", TargetLanguageCode="fr")
        print (result.get('TranslatedText'))