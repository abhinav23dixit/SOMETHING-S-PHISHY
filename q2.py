def test3():
    i=0
    Y=[]
    X=[]
    #count1=count2=0
    #accuracy=0.0
    import csv
    with open('trainset2.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for line in row:
                i=0;
                str=line.split(",");
            Y.append(str[30:33])
            X.append(str[0:30])

    X_test=[]
    pred=[]

    with open('testset2.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for line in row:
                i=0;
                str=line.split(",");
            #Y.append(str[30:33])
            X_test.append(str)

    



    from sklearn.ensemble import RandomForestClassifier


    clf=RandomForestClassifier()
    clf.fit(X,Y)
    pred=clf.predict(X_test)


    with open(r'output2.csv','w',newline='') as output:
        writer=csv.writer(output)
        
        writer.writerows([r] for r in pred)
       

    #print (pred)

    
