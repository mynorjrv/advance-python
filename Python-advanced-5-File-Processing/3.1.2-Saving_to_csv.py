import csv

with open('exported_contacts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    
    writer.writerow(['Name', 'Phone'])
    writer.writerow(['mother', '222-555-101'])
    writer.writerow(['father', '222-555-102'])
    writer.writerow(['wife', '222-555-103'])
    writer.writerow(['mother-in-law', '222-555-104'])
    writer.writerow(['grandmother, grandfather', '222-555-105'])


with open('exported_contacts_dict.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # When writing a Dict, it is necessary to write a header
    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow(
        {
            'Name': 'grandmother, grandfather and auntie', 
            'Phone': '222-555-105'
        }
    )