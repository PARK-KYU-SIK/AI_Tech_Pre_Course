import pandas as pd

def solution(operations) :
    answer = []
    ans = []
    df_o = pd.DataFrame(operations)
    df_o = df_o[0].str.split(' ', expand=True)
    for i in range(0, len(df_o)) :
        j = df_o[0][i]
        k = int(df_o[1][i])
        if j == 'I' :
            ans.append(k)
        else :
            if k == 1 :
                if len(ans) == 0 :
                    pass
                else :
                    a = max(ans)
                    ans.remove(a)
            else :
                if len(ans) == 0 :
                    pass
                else :
                    b = min(ans)
                    ans.remove(b)
    if len(ans) == 0 :
        min_q = 0
        max_q = 0
    else :
        min_q = min(ans)
        max_q = max(ans)
    answer.append(max_q)
    answer.append(min_q)
    return answer