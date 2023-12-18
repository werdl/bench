import time
import os

langs = {
    "python": {
        "build": "",
        "run": "python3"
    },
    "rust": {
        "build": "rustc -o a.out",
        "run": "./a.out"
    },
    "c": {
        "build": "gcc -o a.out",
        "run": "./a.out"
    },
    "c++": {
        "build": "g++ -o a.out",
        "run": "./a.out"
    }
}

scripts = {
    "Hello World": {
        "python": "python/hello.py",
        "rust": "rust/hello.rs",
        "c": "c/hello.c",
        "c++": "cpp/hello.cpp"
    }
}

for name, lang_info in scripts.items():
    print(f"Running suite: {name}")

    for lang, cmd in lang_info.items():
        if langs[lang]["build"] != "":
            os.system(f"{langs[lang]['build']} src/{cmd}")
        cmd_final = langs[lang]["run"]
        if lang in ["python"]:
            cmd_final += "  src/" + cmd
        start = time.time()
        print(f"{lang} - ", end="")
        os.system(cmd_final)
        end = time.time()
        print(f"{end-start}s")
    
    