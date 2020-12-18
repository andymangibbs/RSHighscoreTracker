import requests


def api_pull(keyword):
    url = "https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player=" + keyword
    resp = requests.get(url)
    scores = resp.text.split(',')
    tlist = []
    final_list = []
    for i in range(len(scores)):
        if "\n" in scores[i]:
            tempL = scores[i].split("\n")
            tlist.append(tempL[0])
            scores.insert(i+1, tempL[1])
            final_list.append(tlist)
            tlist = []
        else:
            tlist.append(scores[i])
    del final_list[-1]
    return final_list
