# bench
## benchmarks for various languages

### sample results
- see out.json


### dependencies
- see `tools used`


## tools used
### "oh, but there is a faster \<language> compiler"
- we deliberately chose the most common tool for each language
- as this is the one most devs would use
- any language can be pushed to its limits like this, that is not the point of this project
### "where are the optimisation flags?"
- we chose to exclude them, for the reasons outlined above
### python
- default python3
### rust
- stable rust release
### c
- gcc
### c++
- g++
### haskell
- ghc
### java
- Oracle SDK
### js
- node
### ruby
- default ruby
### c#
- mono
- msc
### php
- default php
### ts
- default npx tsc

## the benchmarks

| language | hello, world | default sorting algorithm | fibonacci (15th term)|
|:-:|:-:|:-:|:-:|
| c |:heavy_check_mark:|:heavy_multiplication_x:|:heavy_check_mark:|
| c++ |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| fortan |:heavy_check_mark:|:heavy_multiplication_x:|:heavy_check_mark:|
| haskell |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| java |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| javascript |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| php |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| python |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| ruby |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| rust |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|
| typescript |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|

  
### key
- :heavy_check_mark: -- done
- :heavy_multiplication_x: -- not available in language (example default sorter in C)
  

