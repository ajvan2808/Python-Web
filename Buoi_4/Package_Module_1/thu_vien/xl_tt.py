import json
import datetime
def doc_file_json(duong_dan):
    f = open(duong_dan, encoding='utf-8')
    du_lieu = json.load(f)
    f.close()
    return du_lieu

def ghi_file_json(duong_dan, noi_dung):
    f = open(duong_dan, 'w', encoding='utf-8')
    json.dump(noi_dung, f, indent=4, ensure_ascii=False)
    f.close()
    return True 
