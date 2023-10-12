import re

def NLP_search(List,Branch):
    def create_short_form(phrase, exclude_words=None):
        words = re.findall(r'\b\w+\b|[()]|\w+[\(\)]*', phrase)
        short_form = ""
        if exclude_words:
            exclude_set = set(exclude_words)
        else:
            exclude_set = set()

        for item in words:
            if item.startswith("(") and item.endswith(")"):
                short_form += item
            elif item.lower() not in exclude_set:
                for word in re.findall(r'\b\w+\b', item):
                    short_form += word[0].upper()

        return short_form


    exclude_words = ["and","or"," "]
    short_form=[]

    for i in List:
        short_form.append(create_short_form(i['Branches'], exclude_words))
    
    for i in List:
        i['Branches'] = [i['Branches']]
        
    for j in range (len(List)):
        List[j]['Branches'].append(short_form[j])
        
    pattern = re.compile(Branch, re.IGNORECASE)

    matching_disciplines = []
    for i in List:
        disciplines = i['Branches']
        for discipline, short_form in disciplines:
            if re.search(pattern, discipline) or re.search(pattern, short_form):
                matching_disciplines.append((discipline, short_form))

    if matching_disciplines:

        print("Matching disciplines:")
        for discipline, short_form in matching_disciplines:
            print(f"{discipline}")