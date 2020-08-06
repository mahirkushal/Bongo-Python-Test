

example = {
            "key1": 1,
            "key2":{
                "key3": 1,
                "key4":{
                    "key5": 4
                }
            }
}

def count_depth(example, a, level = 1):
    str_dic = str(example)
    counter = 0
    for i in str_dic:
        if i == "{":
            counter +=1
            for a in example:
                return(a, counter)
                for b in example[a]:
                    return(b, example[a][b])


print(example, a)

    ##return (counter)

##for b in example:
  ##  if b == "}":
    ##    print(count_depth(dic), b)
      ##  for c in example[b]:
        ##    print(b, example[b][c])
    
        

                    


        

    

