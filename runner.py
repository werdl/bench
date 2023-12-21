import time
import os
import json
import itertools
import threading
import time
import sys

with open("lang-config.json") as langsfp:
    langs = json.load(langsfp)

def conv_to_full(name: str):
    return name.replace('pp', '++').replace('-sharp', '#')

def exclude(*args):
    langs_to_ret = [key for key, value in langs.items()]
    for arg in args:
        if arg!=None:
            langs_to_ret.remove(arg)
    return langs_to_ret

scripts = {
    "Hello World": {
        "filename": "hello",
        "langs": exclude(None)
    },
    "Fibonacci to 15": {
        "filename": "fib",
        "langs": exclude(None)
    },
    "Default Sorter": {
        "filename": "sort",
        "langs": exclude("c")
    }
}

results = {}
passes = 10

# setup runners
os.system("chmod +x runners/*.sh")

for name, lang_info in scripts.items():
    cur_result = {}
    fn = lang_info["filename"]

    for lang in lang_info["langs"]:
        res_s = []
        print(f"{name}::{conv_to_full(lang)}")
        for i in range(passes):
            
            if langs[lang]["build"] != "":
                build_cmd = f"{langs[lang]['build']} src/{lang}/{fn}.{langs[lang]['ext']}"
                os.system(build_cmd + " > /dev/null")

            cmd_final = langs[lang]["run"]

            if langs[lang]["build"]=="" or lang=="ts": # typescript is special
                cmd_final += f" src/{lang}/{fn}.{langs[lang]['ext']}"

            cmd_final += " > /dev/null"

            start = time.time()
            os.system(cmd_final)
            end = time.time()

            res_s.append(end-start)
        done = True

        cur_result[lang] = sum(res_s) / len(res_s)
    results[name] = cur_result
    
for name, res in results.items():
    print(f"For suite '{name}':")
    i=0
    for lang, time_res in dict(sorted(res.items(), key=lambda t: t[1])).items():
        i+=1
        print(f"\t{i} - {conv_to_full(lang)} ({float('%.3g' % time_res)}s)")
        
with open("out.json", "w") as outfile:
    json.dump(results, outfile, indent=4)
    
os.remove("a.out")