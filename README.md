## this language is in development - coming soon 

[![build and test](https://github.com/nitro-lang/nitro/actions/workflows/test.yml/badge.svg)](https://github.com/nitro-lang/nitro/actions/workflows/test.yml)
[![build and publish](https://github.com/nitro-lang/nitro/actions/workflows/build.yml/badge.svg)](https://github.com/nitro-lang/nitro/actions/workflows/build.yml)
[![CodeQL](https://github.com/nitro-lang/nitro/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/nitro-lang/nitro/actions/workflows/github-code-scanning/codeql)

## about nitro
nitro is a general purpose jit compiled language programming language built using python, llvmlite and sly
```
# test program

var a : int32 = 2;
var b : float = 4.2;

func test(x:int,y:float) : float {
  return x + y * 2;
}

func main() {
  print(test(a,b));
}

```

nitro focuses on speed and optimization for more efficient software 
