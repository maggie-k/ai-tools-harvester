from fuzzywuzzy import process #migrate to RapidFuzz

def recommend_tools(user_need, df):

    best_tools=[]

    matches=process.extract(user_need, df['keywords'])
    for i,o in enumerate(matches):
        if matches[i][1]>=50:
            features= matches[i][0]

            tool=df[df['keywords']==features]

            best_tools.append(tool['name'].iloc[0])

    #if best_tools==[]:
        #return ["No tools found for your use case"]

    return best_tools
