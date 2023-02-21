def filter_email(text):
    lines = text.split('\n')
    key_words = ['Message-ID','Date','From','To','Subject',
                 'Mime-Version','Content-Type','Content-Transfer-Encoding',
                 'X-From','X-To','X-cc','X-bcc','X-Folder','X-Origin','X-FileName']
    email=[]
    message=""
    for line in lines:
        count = 0
        for key in key_words:
            if key in line:
                val = line.split(sep=':')
                email.append(val)
                count+=1
                key_words.remove(key)
                break
        if count==0:
            message+=(line+' ')
    email.append(['Body',message])
    return email

def filter_cats(text):
    cat=[]
    lines = text.split('\n')
    for i in range(len(lines) - 1):
        line = lines[i].split(sep=',')
        if (int(line[0]) == 1):
            cat.append(line[0])
            cat.append(line[1])
            cat.append(line[2])
    return cat

def filtered_text(body):
    import re
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    import nltk
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    my_list = body.split()
    i = 0
    while i < len(my_list):
        if '@' in my_list[i]:
            my_list.pop(i)
        else:
            i += 1
    text = ' '.join(x for x in my_list)
    text = text.lower()
    replace = ['forwarded','from','subject','steven','said','enron','california']
    remove = re.compile(r'\b(?:%s)\b'%'|'.join(replace))
    text = remove.sub('',text)
    text = re.sub(r'[^a-z]',' ',text)
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    stem_words = [ps.stem(word) for word in filtered_words]
    words = [word for word in stem_words if len(word)>3]
    text = ' '.join(x for x in words)
    return text

def load_data(content,cat_content,temp):
    key = temp[0]
    email = filter_email(content)
    key_words = ['Message-ID', 'Date', 'From', 'To', 'Subject',
                 'Mime-Version', 'Content-Type', 'Content-Transfer-Encoding',
                 'X-From', 'X-To', 'X-cc', 'X-bcc', 'X-Folder', 'X-Origin', 'X-FileName']
    while email:
        item = email[0]
        if len(key_words)==0:
            email.pop(0)
            temp.append(item[1])
            break
        else:
            key_item = key_words[0]
            if item[0] == key_item:
                email.pop(0)
            key_words.pop(0)
    cat = filter_cats(cat_content)
    for x in cat:
        temp.append(x)
    body = temp[1]
    category = int(temp[3])
    data=[]
    clean_text = filtered_text(body)
    data.append(clean_text)
    data.append(category)
    return data
