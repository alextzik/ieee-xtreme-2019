# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split('\n'))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
    
# numpy and scipy are available for use
import numpy
import scipy
import json
import decimal

def calc_if(data_17, data_18):
    numerator = int(data_17['citations']) + int(data_18['citations'])
    denominator = int(data_17['articleCounts']) + int(data_18['articleCounts'])
    impact_factor = numerator/denominator
    return decimal.Decimal("{0:.2f}".format(impact_factor))

def sort_results():
    global journal_names, impact_factors
    
    n = len(journal_names)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if impact_factors[j] < impact_factors[j+1] :
                impact_factors[j], impact_factors[j+1] = impact_factors[j+1], impact_factors[j]
                journal_names[j], journal_names[j+1] = journal_names[j+1], journal_names[j]
            elif impact_factors[j] == impact_factors[j+1]:
                if journal_names[j] > journal_names[j+1]:
                    impact_factors[j], impact_factors[j+1] = impact_factors[j+1], impact_factors[j]
                    journal_names[j], journal_names[j+1] = journal_names[j+1], journal_names[j]
                
# read input data count
record_count = get_number()

# read publications
data = json.loads(get_word())

# read journal issues
issues = []
for i in range (record_count - 1):
    issue = get_word()
    issues.append(json.loads(issue))

# create dict for specific journal fields, for faster access
journals = {}
journal_ids = []
for publication in data['publications']:
    jid = publication['publicationNumber']
    journal_ids.append(jid)
    journals[jid] = {}
    journals[jid]['publicationTitle'] = publication['publicationTitle']
    journals[jid]['articleCounts'] = publication['articleCounts']
    for article in publication['articleCounts']:
        year = article['year']
        journals[jid][year] = {}
        journals[jid][year]['articleCounts'] = article['articleCount']
        journals[jid][year]['citations'] = 0
        journals[jid].pop('articleCounts', None)

# count the citations for each year, for each journal
for issue in issues: 
    articles = issue["paperCitations"]["ieee"]
    for article in articles:
        jid = article['publicationNumber']
        year = article['year']
        try:
            journals[jid][year]['citations'] += 1
        except KeyError:
            pass
        
# calculate impact factor for each

# print(json.dumps(journals, indent=2))
    

# publications = data['publications']
journal_names = []
impact_factors = []
for jid in journal_ids:
    journal = journals[jid]
    # print(journal)
    impact_factor = calc_if(journal['2017'], journal['2018'])
    journal_names.append(journal['publicationTitle'])
    impact_factors.append(impact_factor)
    
sort_results()

for i in range (len(journal_ids)):
    print(f"{journal_names[i]}: {impact_factors[i]}")

# print(journal_ids)
# a = get_number()
# b = get_number()

# res = a + b
# print(res)
