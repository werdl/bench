# bench
## benchmarks for various languages

### get result
- install deps
- then run `python3 runner.py <passes>` where passes is how many times to run each test (we reccommend 10)


### dependencies
- see `tools used`


## tools used
### "oh, but there is a faster \<language> compiler"
- we deliberately chose the most common tool for each language
- as this is the one most devs would use
- any language can be pushed to its limits like this, that is not the point of this project
### "where are the optimisation flags?"
- we chose to exclude them, for the reasons outlined above
### "where is <lang>?"
- if you want to add a language (or script), see `CONTRIBUTING.md`

### c
- gcc
### c#
- mcs
### cobol
- GnuCOBOL
### c++
- g++
### fortran
- GNU Fortran
### go
- default go from go.dev
### haskell
- ghc
### java
- Any SDK (I use Oracle)
### javascript
- node
### kotlin
- default kotlin SDK
### lisp
- SBCL, for ANSI Common Lisp
### php
- php interpreter
### python
- python3 default
### ruby
- default ruby interpreter
### typescript
- tsc (from npm)
### v
- default v compiler

## the benchmarks

| language | Hello, World! | default sorting algorithm | fibonacci (15th term)|
|:-:|:-:|:-:|:-:|
| c |:white_check_mark:|:x:|:white_check_mark:|
| c# |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| cobol |:white_check_mark:|:x:|:white_check_mark:|
| c++ |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| fortan |:white_check_mark:|:x:|:white_check_mark:|
| go |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| haskell |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| java |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| javascript |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| kotlin |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| php |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| python |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| ruby |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| rust |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| typescript |:white_check_mark:|:white_check_mark:|:white_check_mark:|
| v |:white_check_mark:|:white_check_mark:|:white_check_mark:|


  
### key
- :white_check_mark: -- done
- :x: -- not available in language (example default sorter in C)
  

