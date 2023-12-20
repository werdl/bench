import time
import os
import json
import subprocess

langs = {
    "python": {
        "build": "",
        "run": "python3",
        "ext": "py"
    },
    "rust": {
        "build": "rustc -o a.out",
        "run": "./a.out",
        "ext": "rs"
    },
    "c": {
        "build": "gcc -o a.out",
        "run": "./a.out",
        "ext": "c"
    },
    "cpp": {
        "build": "g++ -o a.out",
        "run": "./a.out",
        "ext": "cpp"
    },
    "haskell": {
        "build": "ghc -o a.out",
        "run": "./a.out",
        "ext": "hs"
    },
    "java": {
        "build": "",
        "run": "java",
        "ext": "java"
    },
    "js": {
        "build": "",
        "run": "node",
        "ext":"js"
    },
    "ruby": {
        "build": "",
        "run": "ruby",
        "ext": "rb"
    }
}

scripts = {
    "Hello World": {
        "filename": "hello",
        "langs": ["python", "rust", "c", "cpp", "haskell", "js", "ruby", "java"]
    },
    "Fibonacci to 15": {
        "filename": "fib",
        "langs": ["python", "rust", "c", "cpp", "haskell", "js", "ruby", "java"]
    },
    "Default Sorter": {
        "filename": "sort",
        "langs": ["cpp", "rust", "python", "haskell", "js", "ruby", "java"]
    }
}

results = {}

for name, lang_info in scripts.items():
    cur_result = {}
    fn = lang_info["filename"]

    for lang in lang_info["langs"]:
        print(f"{name}::{lang}")
        build_cmd = f"{langs[lang]['build']} src/{lang}/{fn}.{langs[lang]['ext']}"
        
        if langs[lang]["build"] != "":
            os.system(build_cmd + " > /dev/null")

        cmd_final = langs[lang]["run"]

        if langs[lang]["build"]=="":
            cmd_final += f" src/{lang}/{fn}.{langs[lang]['ext']}"

        cmd_final += " > /dev/null"

        start = time.time()
        os.system(cmd_final)
        end = time.time()

        cur_result[lang] = end-start
    results[name] = cur_result
    
for name, res in results.items():
    print(f"For suite '{name}':")
    i=0
    for lang, time_res in dict(sorted(res.items(), key=lambda t: t[1])).items():
        i+=1
        print(f"    {i} - {lang} ({float('%.3g' % time_res)}s)")
        
with open("out.json", "w") as outfile:
    json.dump(results, outfile, indent=4)
    
os.remove("a.out")